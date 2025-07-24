#!/usr/bin/env python3

import boto3
import uuid
from botocore.exceptions import ClientError

## https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-environment-variables

## boto3.client() = low level interface that maps directly to AWS service APIs and returns raw dict from AWS API
## botot3.resource() = high level OOP interfaces


# s3_client = boto3.client('s3',aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
#                       aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
#                       region_name="us-east-1")

# response = s3_client.list_buckets() # Raw dict response
# buckets =  response["Buckets"]
# print(buckets)


# s3 = boto3.resource('s3') 
# for bucket in s3.buckets.all():  # Returns bucket objects
#     print(bucket.name)

##############################
## create bucket
## push a file into a bucket
## delete bucket

# create client
s3 = boto3.resource('s3')

def create_bucket(client, bucket_name):
    # generate unique uuid
    suffix = str(uuid.uuid4()).split("-")[0]
    return client.create_bucket(Bucket = f"{bucket_name}-{suffix}")

def list_buckets(client):
    '''https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/service-resource/buckets.html'''
    for b in client.buckets.all(): # return an interator object with all buckets 
        print(b)

def delete_bucket(client,bucket_name):
    '''https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/delete.html'''
    bucket = client.Bucket(bucket_name)
    
    try:
        bucket.delete()
    except ClientError as err:
        print(f"Bucket name does not exist:{err.response['Error']}")
        return 



if __name__ == "__main__":

    # list_buckets(s3)
    # create_bucket(s3, bucket_name = "titi")
    list_buckets(s3)
    delete_bucket(s3,'tto-bbb5c0ca')
    list_buckets(s3)