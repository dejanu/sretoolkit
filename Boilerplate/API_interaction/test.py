#!/usr/bin/env python3

import boto3
from botocore.exceptions import ClientError

def list_buckets(client):
    """ list buckets """
    return ([b["Name"] for b in s3client.list_buckets()['Buckets']])

def create_bucket(client,bucket_name):
    """create bucket """
    import uuid
    bucket_unique = f"{bucket_name}-{str(uuid.uuid4()).split('-')[0]}"
    print(f"Creating bucket: {bucket_unique}")
    return client.create_bucket(Bucket = bucket_unique,
                                CreateBucketConfiguration = { "LocationConstraint" : "us-west-1" }
                                )   

def delete_bucket(client,bucket_name):
    """ delete bucket """
    try:
        return client.delete_bucket(Bucket = bucket_name)
    except ClientError as err:
        print("Error deleting bucket:", err)

def delete_objects(client,bucket_name):
    """ delete objects in a bucket """
    for obj in client.list_objects_v2(Bucket = bucket_name).get('Contents'):
        print(obj)
        ## delete objects in bucket: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html
        client.delete_objects(Bucket=bucket_name,
                                 Delete = { 
                                     'Objects': [{'Key': f'{obj["Key"]}'} ]
                                        }
                                )

def transfer_file(client,bucket_name, filename, upload = False):
    """ upload or download file to a bucket"""
    import os
    if upload == True: #uploading file
        for p,d,f in os.walk(os.getcwd()):
            for ffile in f:
                if ffile ==  filename:
                    print(os.path.join(p,ffile))
                    with open(filename,'rb') as fo:
                        return client.upload_fileobj(fo,bucket_name,f"{bucket_name}-object")
    else: # downloading file: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
        # list objects in bucket: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html#
        print (f"Objects in bucket: {client.list_objects_v2(Bucket = bucket_name).get('Contents')}")
        return client.download_file(bucket_name,'testme-0c5f2c52-object',filename)

if __name__ == "__main__":
    
    s3client =  boto3.client('s3', region_name = "us-west-1")
    # a = create_bucket(s3client,"testme")
    print(list_buckets(s3client)) 
    # transfer_file(s3client,'testme-0c5f2c52','new.json',upload=False)
    # print(delete_objects(s3client,'test-ecbb756d'))
    delete_bucket(s3client,'test-ecbb756d')
    print(list_buckets(s3client)) 