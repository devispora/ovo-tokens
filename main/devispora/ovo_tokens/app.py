import json

# import requests
from devispora.ovo_tokens.service.token_generator import generate_redeem_code


def lambda_handler(event, context):
    print(event)
    body = json.loads(json.loads(event['body']))
    redeem_code = generate_redeem_code(body)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "redeem_code": redeem_code
        }),
    }
