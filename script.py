import boto3
import botocore
import sys
import time

print(sys.argv[1])
TABLE_NAME = "FileData"
s3 = boto3.resource('s3')
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

#retrive data from DB

response = dynamodb_client.get_item(
    TableName=TABLE_NAME,
    Key={
        'id': {'N': sys.argv[1]}
    }
)
print(response['Item'])

temp = response['Item']['filePath']['S'].split('/')
BUCKET_NAME = temp[0]
KEY = temp[1]

print(BUCKET_NAME)
print(KEY)

#download file from S3
s3.Bucket(BUCKET_NAME).download_file(KEY, KEY)

#update the name and upload it on S3

key_list = KEY.split('.')
new_name = key_list[0]+"_output"+key_list[1]
s3.meta.client.upload_file(KEY, BUCKET_NAME, new_name)

#add new entry in DB
data = dynamodb_client.put_item(
    TableName = TABLE_NAME,
    Item= {
        'id': {
          'N': str(time.time())
        },
        'inputData': {
          'S': ''
        },
        'filePath': {
          'S': new_name
        }
    })