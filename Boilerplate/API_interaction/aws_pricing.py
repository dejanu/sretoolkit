#!/usr/bin/env python3
# AWS SDK for Python (Boto3)

import boto3
import json
import os

def get_pricing_with_terms():
    pricing_client = boto3.client('pricing', 
                                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
                                region_name="us-east-1")
    
    response = pricing_client.get_products(
        ServiceCode="AmazonS3",
        Filters=[
            {
                'Field': 'location',
                'Type': 'TERM_MATCH',
                'Value': 'US East (N. Virginia)'
            },
            {
                'Field': 'storageClass',
                'Type': 'TERM_MATCH',
                'Value': 'General Purpose'
            }
        ],
        FormatVersion='aws_v1',
        MaxResults=5
    )
    
    for price_item in response.get('PriceList', []):
        pricing_data = json.loads(price_item)
        
        # Extract product info
        product = pricing_data.get('product', {})
        sku = product.get('sku')
        attributes = product.get('attributes', {})
        
        print(f"SKU: {sku}")
        print(f"Storage Class: {attributes.get('storageClass', 'N/A')}")
        print(f"Location: {attributes.get('location', 'N/A')}")
        
        # Extract actual pricing from terms
        terms = pricing_data.get('terms', {})
        on_demand = terms.get('OnDemand', {})
        
        for term_key, term_data in on_demand.items():
            price_dimensions = term_data.get('priceDimensions', {})
            for dim_key, dim_data in price_dimensions.items():
                price_per_unit = dim_data.get('pricePerUnit', {})
                usd_price = price_per_unit.get('USD', 'N/A')
                unit = dim_data.get('unit', 'N/A')
                description = dim_data.get('description', 'N/A')
                
                print(f"  Price: ${usd_price} per {unit}")
                print(f"  Description: {description}")
        print("-" * 50)

if __name__ == "__main__":
    get_pricing_with_terms()
