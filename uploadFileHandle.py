import json
import boto3
import time

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    
    key = time.time()
    input_text = event["inputText"]
    file_path = event["filePath"]
    
    if input_text == '' or file_path == '':
        return{
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE'
            },
            'body': json.dumps({'message': 'Fail'})
        }
    
    
    data = client.put_item(
    TableName='FileData',
    Item= {
        'id': {
          'N': str(key)
        },
        'inputData': {
          'S': 
        },
        'filePath': {
          'S': event["filePath"]
        }
    }
    )
    
    print(event)
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin' : '*',
    '       Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE'
        },
        'body': json.dumps({'message': 'Success'})
    }
    return response
    
