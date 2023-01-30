import logging
import boto3
import json
from botocore.exceptions import ClientError
def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.run_instances(ImageId='ami-0742b4e673072066f', InstanceType='t2.micro', MaxCount=1, MinCount=1)
