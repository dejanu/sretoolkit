
#!/usr/bin/env bash

# CreatedSince: how long vs. CreatedAt: exact timestamp
echo -e "\e[36mYou have \e[33m$(docker system info --format '{{ .Images}}')\e[36m images on your machine:\e[0m"
docker images --format "{{ .Repository }}:{{ .Tag }} -----> Created: {{ .CreatedSince }}"

echo -e "\e[36mPass the image name to scan: i.e repo:tag\e[0m"
read image_name

echo -e "\e[36mScanning image...${image_name}, Report will be generated at /tmp/report/report_$(date +%d_%m_%Y_%S).html\e[0m"
timestamp=$(date +%d_%m_%Y_%S)
# trivy scan
mkdir -p /tmp/report
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $HOME/Library/Caches:/root/.cache/ -v /tmp/report:/tmp aquasec/trivy:latest image \
-f template --template "@contrib/html.tpl" -o /tmp/report_"${timestamp}".html ${image_name}