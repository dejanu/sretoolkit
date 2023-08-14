#!/bin/bash

#######################################################
## Azure AKS:                                        ##
## Create AKS on the fly based on env vars           ##
## AZLOCATION,AZGROUP,AKSNAME                        ##     
#######################################################

# list resource groups in the current subscription
az group list -o table

# list AKS clusters
az aks list -o table

# check if the variables are set as env vars if not default to the values az_location="westeurope" az_resource_group="demoSRE" az_cluster_name="demoAKS"
az_location=${AZLOCATION}:-"westus"}
az_resource_group=${AZGROUP:-"demoSRE"}
az_cluster_name=${AKSNAME:-"demoAKS"}

# check if resource group exists if not create it
if [ -z "$(az group exists -n $az_resource_group)" ]; then
    echo "Resource group $az_resource_group does not exist. Creating it..."
    az group create --name $az_resource_group --location $az_location
else
    echo "Resource group $az_resource_group already exists."
fi

# create AKS cluster with 2 worker nodes
az aks create \
    --resource-group $az_resource_group \
    --name $az_cluster_name \
    --node-count 2 \
    --enable-addons monitoring \
    --generate-ssh-keys

# check if the return code of the previous command is 0
if [ $? -eq 0 ]; then
    echo "AKS cluster $az_cluster_name created successfully."
else
    echo "AKS cluster $az_cluster_name creation failed."
fi

# get credentials for the cluster
az aks get-credentials --resource-group $az_resource_group --name $az_cluster_name

# list AKS clusters
az aks list -o table