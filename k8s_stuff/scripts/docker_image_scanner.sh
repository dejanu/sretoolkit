
#!/usr/bin/env bash



# create function called scan_image which takes one argument: the image name
scan_image() {
    # trivy scan
    docker run --rm -v trivy-cache:/root/.cache/ -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image ${image}
    # docker run --rm \
        # --volume /var/run/docker.sock:/var/run/docker.sock \
        # --name GrypeScanner anchore/grype:latest \
        # ${i}
    
    #
}

# echo to stdout images on host
images=$(docker system info --format '{{ .Images}}')
echo "You have ${images} images on your machine:"
docker images

# loop through images and interactively ask the user if they want to scan the image
for image in $(docker images --format "{{.Repository}}:{{.Tag}}")
    do
        echo "Do you want to image ${image} ? (y/n)"
        read answer
        if [ "$answer" == "y" ]
        then
            echo "Scanning image: ${image}"
            scan_image ${image}
        else
            echo "Skipping image: ${image}"
        fi
    done

