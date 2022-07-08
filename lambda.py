import json

def lambda_handler(event, context):
    print('---')
    print(event)
    try:
        if event['temperature']!='':
            #TODO:ここからdynamoDBに書き込み
            return {
                'statusCode': 200,
                'body': str(event['temperature'])
            }
    except:
        return {
                'statusCode': 200,
                'body': str(event)
        }
