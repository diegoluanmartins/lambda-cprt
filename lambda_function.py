import json
import log

def lambda_handler(event, context):
    log.log(event)
    return {
        'statusCode': 200,
        'hello': 'world',
        'body': json.dumps(event)
    }
