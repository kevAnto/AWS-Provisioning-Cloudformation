import logging
import boto3
import json
from botocore.exceptions import ClientError
def lambda_handler(event, context):
    client = boto3.client('s3')
    response = client.create_bucket(Bucket='kev-ac-bucket')