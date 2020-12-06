import json
import boto3


def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        bucketResponse = s3Client.list_buckets()
    except Exception as e:
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! there are '
                           + str(len(bucketResponse["Buckets"])) + ' bukets')
    }