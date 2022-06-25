import json
import boto3
import time
 
AMI = 'ami-0367dc0ab134ae1c7'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'jashminmpatel'
REGION = 'us-east-1'
BUCKET_NAME = 'asu-serverless-appbucket'
ec2 = boto3.client('ec2', region_name=REGION)
 
def lambda_handler(event, context):

   #getting data from Dynamodb trigger - from json object
   
   data_id = event['Records'][0]['dynamodb']['Keys']['id']['N']
   data_input = event['Records'][0]['dynamodb']['NewImage']['inputData']['S']
   #data_id = '1656058439.884117'
   #data_input = 'testing'
   
   if data_input == '':
      return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Failed'})
    }
      
   print(data_input)
   print(event)
   
   #creating new EC2 instance
   
   instance = ec2.run_instances(
   ImageId=AMI,
   InstanceType=INSTANCE_TYPE,
   KeyName=KEY_NAME,
   MaxCount=1,
   MinCount=1
   )
   
   time.sleep(600)
  
   waiter = ec2.get_waiter('instance_running')
   print ("New instance created:")
   instance_id = instance['Instances'][0]['InstanceId']
   print (instance_id)
   
   
   #attaching a role to EC2 instance so it can run script 
   response = ec2.associate_iam_instance_profile(
      IamInstanceProfile={
         'Name': 'ec2_ssm'
      },
         InstanceId=instance_id
      )
   print("permission assigned")
   
   time.sleep(60)
   
   # run remote command in EC2 by ssm.
   
   ssm = boto3.client("ssm")
                
   print(InstanceId)
   commands = ["curl -O https://asu-serverless-appbucket.s3.amazonaws.com/script.py",
   	"python script.py " + data_id]
   	
   response = ssm.send_command(
      InstanceIds=[instance_id],
      DocumentName="AWS-RunShellScript",
      Parameters={
          "commands": commands
      },  
   )
  
   command_id = response["Command"]["CommandId"]
   
   #fetching command output
   output = ssm.get_command_invocation(CommandId=command_id, InstanceId=instance_id)
   print(output)
   print(instance['Instances'][0]['State'])

   #terminating the newly created instance.
   
   ec2.terminate_instances(InstanceIds=[instance_id])
   print('Terminated instance: ' + str(instance_id))
   
   return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Success'})
    }