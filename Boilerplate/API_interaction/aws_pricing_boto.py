#!/usr/bin/env python3

# AWS SDK for Python (Boto3)
import boto3
import os
import json

boto3_client = boto3.client('pricing',aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                      aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
                      region_name="us-east-1")


response = boto3_client.get_products(ServiceCode="AmazonS3")

price_list = response.get("PriceList")
for item in price_list:
    parsed = json.loads(item)
    print(json.dumps(parsed, indent=2))
