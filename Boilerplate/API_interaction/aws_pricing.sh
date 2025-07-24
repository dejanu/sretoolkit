#!/usr/bin/env bash

# curl to get services https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json
curl -s https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json -o index.json

# In the service index file, you can search for the service to find its prices
# let the user choose a service
echo "Available AWS services:"
jq -r '.offers | keys[]' index.json | nl
read -p "Enter the number of the service you want to query: " service_number
service=$(jq -r ".offers | keys[${service_number} - 1]" index.json)
# get the service index file
curl -s "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/${service}/index.json" -o "${service}_index.json"


echo "Available offers for ${service}:"
jq -r '.versions | to_entries[] | "\(.key): \(.value)"' "${service}_index.json" | nl
read -p "Enter the number of the offer you want to query: " offer_number

# for the number selected by the user return the offer url i.e. /offers/v1.0/aws/AmazonS3/20250717165314/index.json
offer=$(jq '.versions["20250717165314"].offerVersionUrl' "${service}_index.json" | tr -d '"')
echo "Selected offer: ${offer}" 
url="https://pricing.us-east-1.amazonaws.com${offer}"
echo "Offer URL: ${url}"

# get the offer file https://pricing.us-east-1.amazonaws.com/{offer}
curl -L "https://pricing.us-east-1.amazonaws.com${offer}" -o "${service}_offer.json"

# open the offer file in jq and pretty print it
jq '.' "${service}_offer.json"