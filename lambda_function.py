import json
import log
import os
  
def lambda_handler(event, context):
    log.log("Event: " + json.dumps(event))
    return {
        'statusCode': 200,
        'ENV_VAR_1': os.environ['ENV_VAR_1'],
        'body': json.dumps(event)
    }
