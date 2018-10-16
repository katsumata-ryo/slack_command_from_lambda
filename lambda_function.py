from slackclient import SlackClient
import os

def lambda_handler(event, context):
    slack_token = os.environ['TOKEN_ID']
    sc = SlackClient(slack_token)

    sc.api_call(
        "chat.command",
        channel="CAxxxxxx",
        command='/slack_command',
    )
    
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': '{"message": "Hello from AWS Lambda"}'
    }
