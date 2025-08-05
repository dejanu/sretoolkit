#!/bin/bash


# Quickly assess docker images using docker search and Docker Official images

# Usage: ./reg_finder.sh <image_name> Example: ./reg_finder.sh alpine

${IMAGE_NAME}=$1

# find the current registry
# defaults to Registry: https://index.docker.io/v1/
# index.docker.io hosts the Docker implementation by DockerHub.
docker info

#  search for images containing a given string
docker search --format "table {{.Name}}\t{{.StarCount}}\t{{.IsOfficial}}" ${IMAGE_NAME}

# # get token to be able to talk to Docker Hub
# TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${DUSER}'", "password": "'${DPASS}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
# curl -s -H "Authorization: Bearer ${TOKEN}" https://hub.docker.com/v2/repositories/${DUSER}/?page_size=10000 

# hub.docker.com hosts the rich DockerHub specific APIs.
curl -s https://hub.docker.com/v2/namespaces/library/repositories/${IMAGE_NAME}/tags/?page_size=10000 | jq -r '.results|.[]|.name'


docker scout quickview ${IMAGE_NAME}
docker scout recommendations ${IMAGE_NAME} 
docker scout cves ${IMAGE_NAME} 