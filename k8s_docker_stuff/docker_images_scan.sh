
#!/usr/bin/env bash

# This script will list and scan all images from the machine

# save the output of docker images command to a variable

images=$(docker system info --format '{{ .Images}}')

# echo to stdout the images
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
        else
            echo "Skipping image: ${image}"
        fi
    done