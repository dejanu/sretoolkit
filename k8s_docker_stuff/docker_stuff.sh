#!/bin/bash

echo -e "\033[1;4;32;41mDocker daemon: \e[0m";
docker system info
echo -e "\033[1;4;32;41mRunning Containers: \e[0m";
docker ps --format 'table {{.Names}}\t{{.Status}}'
echo "----------------------------------------------------"
docker system df