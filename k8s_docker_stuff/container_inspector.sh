#!/usr/bin/env bash

# get no of images
docker system info --format '{{ .Images}}'

# get images
docker images

images=$(docker images --format='{{.Repository}}:{{.Tag}}')
for i in $images; do
    echo -e "Scan the image: ${i} y/n"
    read answer
    if [ $answer == "y" ]; then
        # docker run --rm \
        # --volume /var/run/docker.sock:/var/run/docker.sock \
        # --name GrypeScanner anchore/grype:latest \
        # ${i}
        ## trivy scan
        docker run --rm -v trivy-cache:/root/.cache/ -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image ${i}
    else
        echo "no scan"
    fi
done