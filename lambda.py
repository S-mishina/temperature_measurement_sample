from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
import json
import boto3

def lambda_handler(event, context):
    print('---')
    print(event)
    if len(event)!=0:
        #TODO:環境変数に置き換える
        dynamodb = boto3.resource('')
        table = dynamodb.Table('')
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
