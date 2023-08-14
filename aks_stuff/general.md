# General stuff


### AKS fun stuff

```bash
# get subscriptions
az account list -o table --all

# set subscription 
az account set --subscription <subscription_ID>

# verify that you set the subscription
az account show -o table

# list resource groups in the subscription
az group list -o table

# list resources from resource group
az resource list --query "[?resourceGroup=='RESOURCE_GROUP_NAME']" -o table

# get available k8s versions for AKS (available versions in your target region)
az aks get-versions --location westeurope | jq ".orchestrators[] | .orchestratorVersion"
az aks get-versions --location westeurope --output table

# get avaible versions for your AKS cluster
az aks get-upgrades --resource-group <RESOURCE_GROUP_NAME> --name <Kubernetes_service_AKS_CLUSTER_NAME> --output table

# check AKS/K8s nodepool (what type VMSS what Surge)
az aks show --resource-group <RESOURCE_GROUP_NAME> --name <Kubernetes_service_AKS_CLUSTER_NAME> --query agentPoolProfiles
az aks nodepool list --cluster-name <Kubernetes_service_AKS_CLUSTER_NAME> --resource-group <RESOURCE_GROUP_NAME> 

# confirm upgrade and check cluster 
az aks show --resource-group <RESOURCE_GROUP_NAME> --name <Kubernetes_service_AKS_CLUSTER_NAME> --output table

# check control plane and nodes k8s version
az aks show -g <RESOURCE_GROUP_NAME> -n <Kubernetes_service_AKS_CLUSTER_NAME> | grep -E "orchestratorVersion|kubernetesVersion"

# details of Azure resource consumption as an invoice for the selected resource 
#az consumption usage list --subscription "$subscription_id" --query "[].{Name:instanceName, Product:product, Usage:usageQuantity}" -o table
az consumption budget list --subscription "$subscription_id" -o table
az consumption budget list -g '$resource_group' -o table

# run a container image on the node to connect to it. The following command starts a privileged container on your node and connects to it.
kubectl debug node/aks-nodepool1-37663765-vmss000000 -it --image=mcr.microsoft.com/dotnet/runtime-deps:6.0
```

* If you have a low compute quota available, the upgrade may fail, because when you upgrade an AKS cluster, extra resources are temporarily consumed, resources like available IP addresses in a virtual network subnet or virtual machine vCPU quota.

* To speed up the upgrade you can increasing the max surge for your node pool (extra nodes during the upgrade)

* The upgrade will trigger a CORDON (mark node as unschedulable) followed by a DRAIN if the exiting node (evicting the Pods) and finally UPGRADING the node.

### Links:

- https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster?tabs=azure-cli
- https://learn.microsoft.com/en-us/azure/quotas/regional-quota-requests
- Zero downtime upgrade: https://omichels.github.io/zerodowntime-aks.html
- Cheeatos page: https://dejanu.github.io/cheeatos/azure.html

