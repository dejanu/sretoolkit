
#!/usr/bin/env bash

# CreatedSince: how long vs. CreatedAt: exact timestamp
echo "You have $(docker system info --format '{{ .Images}}') images on your machine:"
docker images --format "{{ .Repository }}:{{ .Tag }} -----> Created: {{ .CreatedSince }}"

echo "Pass the image name to scan: "
read image_name

echo -e "\e[33mScanning image...${image_name}, will be generated at /tmp/report_${date +%d_%m_%Y_%S}.html\e[0m"

# trivy scan
mkdir -p /tmp/report
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $HOME/Library/Caches:/root/.cache/ -v /tmp/report:/tmp aquasec/trivy:latest image \
-f template --template "@contrib/html.tpl" -o /tmp/report_${image_name}.html ${image_name}


# scan_image() {
#     # trivy scan
#     docker run --rm -v trivy-cache:/root/.cache/ -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image ${image}
#     # docker run --rm \
#         # --volume /var/run/docker.sock:/var/run/docker.sock \
#         # --name GrypeScanner anchore/grype:latest \
#         # ${i}
    
#     #
# }


# # loop through images and interactively ask the user if they want to scan the image
# for image in $(docker images --format "{{.Repository}}:{{.Tag}}")
#     do
#         echo "Do you want to image ${image} ? (y/n)"
#         read answer
#         if [ "$answer" == "y" ]
#         then
#             echo "Scanning image: ${image}"
#             scan_image ${image}
#         else
#             echo "Skipping image: ${image}"
#         fi
#     done

