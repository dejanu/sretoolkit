#!/usr/bin/env python3


import boto3

# create resource
client = boto3.client('s3')



# import uuid

# mybucket = resource.Bucket(f"test-{str(uuid.uuid4()).split('-')[0]}")

# mybucket.create(
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-west-1'
#     }
# )

# print(f"Bucket {mybucket.name} created successfully.")

import os

def read_file(filename, bucket):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    for p,d,f in os.walk(os.getcwd()):
        for file in f:
            if file == filename:
                print(os.path.join(p,file))
                with open(os.path.join(p,file),'rb') as f:
                    r = client.upload_fileobj(f,bucket,"objttest")




if __name__ == "__main__":
    read_file('upload.txt','test-3e0a8259')