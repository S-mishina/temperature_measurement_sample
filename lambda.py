from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
import os
import json
import boto3

def lambda_handler(event, context):
    print('---')
    print(event)
    if len(event)!=0:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ['DB_NAME'])
        now = datetime.today()
        day=now.strftime('%Y/%m/%d')
        date=now.strftime('%H:%M:%S')
        #ここでデータを追加する。
        table.put_item(Item={'day': str(day) ,'date': str(date),'temperature':str(event['temperature'])})
        return {
            'statusCode': 200,
            'body': str(event['temperature'])
        }
    else:
        return {
            'statusCode': 200,
            'body': "no data"
        }
