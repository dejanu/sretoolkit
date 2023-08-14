#!/usr/bin/env bash

# This script will inspect a pod and return the following information:
# Containers running in the pod
# Images used by the containers
# Logs for each container

# Usage: ./pod_inspector.sh <namespace>
# Check if namespace is provided
if [ -z "$1" ]
then
    echo "Usage: ./pod_inspector.sh <namespace>"
    echo "Current namespaces are:"
    kubectl get ns
    exit 1
fi 

# Get pods in the namespace
kubectl get pods -n $1 -oname

# Get pod name
echo "Enter pod name:"
read pod_name

# Get containers running in the pod
containers=$(kubectl get pod $pod_name -n $1 -o jsonpath="{.spec.containers[*].name}")
images=$(kubectl get pod $pod_name -n $1 -o jsonpath="{.spec.containers[*].image}")

# write container with images to stdout
echo "Containers running in the pod:"
echo $containers
echo "Images used by the containers:"
echo $images