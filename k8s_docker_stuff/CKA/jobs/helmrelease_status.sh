#!/bin/bash

####################################################
## helm-release via flux or argo: kubectl get hr  ##
## helm-release via helm: helm list               ##  
####################################################

# get the status of all helm releases
kubectl get hr -A -o jsonpath='{range .items[*]}{.metadata.namespace}/{.metadata.name}: {.status.releaseStatus}{"\n"}{end}'

# iterate over all namespaces and if the status is not deployed, then delete the helm release
for ns in $(kubectl get ns -o jsonpath='{.items[*].metadata.name}'); do
    for hr in $(kubectl get hr -n $ns -o jsonpath='{.items[*].metadata.name}'); do
        # save the status in variable
        status=$(kubectl get hr -n $ns $hr -o jsonpath='{.status.releaseStatus}')
        echo "Checking $hr in $ns namespace with status $status"
        # if the status is not deployed, then delete the helm release
        # if [[ $(kubectl get hr -n $ns $hr -o jsonpath='{.status.releaseStatus}') != "deployed" ]]; then
        if [ "$status" != "deployed" ]; then
            # kubectl delete hr -n $ns $hr
            echo "Deleted $hr in $ns namespace"
        fi
    done
done