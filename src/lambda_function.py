import boto3
import os

table = boto3.resource('dynamodb').Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='ADD #count :inc',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':inc': 1}
    )
    resp = table.get_item(Key={'id': 'visitor_count'})
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': str(resp['Item']['count'])
    }
