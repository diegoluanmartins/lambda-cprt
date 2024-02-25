import json
import log

def lambda_handler(event, context):
    log.log("Event: " + event)
    return {
        'statusCode': 200,
        'hello': 'world',
        'cprt':'666',
        'body': json.dumps(event)
    }
