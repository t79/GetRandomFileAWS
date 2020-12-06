import json
import boto3

bucketName = "filearchive.t79.it"

def lambda_handler(event, context):
    s3Client = boto3.client('s3')

    try:
        objectsResponse = s3Client.list_objects(Bucket=bucketName)

        fileNamesList = []
        for object in objectsResponse["Contents"]:
            fileNamesList.append(object["Key"])

    except Exception as e:
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! there are '
                           + str(len(fileNamesList)) + ' objects: '
                           + " ".join(name for name in fileNamesList))
    }