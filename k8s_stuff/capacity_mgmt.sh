#!/usr/bin/env bash

#############################################################
# Purpose: wrapper for inspecting Requests/Limits for Pods ##
# @dejanualex                                              ##
#############################################################

# set grep color to yellow
export GREP_COLORS='ms=01;33'

# Options for inspecting resource usage
echo -e "\n Please select desired resource to inspect:\n 1. CPU[millicores] \n 2. Memory[bytes] \n"
read -r option
# if option is 1 set resource variable to CPU
if [ "${option}" == "1" ]; then
    resource="cpu"
# if option is 2, set resource variable to CPU
elif [ "${option}" == "2" ]; then
    resource="memory"
else
    echo -e "\e[0;31m Please select a valid option \e[0m"
    exit 1
fi

### NODE LEVEL
# read node name
echo -e "\n Available nodes are:\n $(kubectl get nodes -o=custom-columns=NODES:.metadata.name) \n"
echo -e "\n Please write the name of the node for which you want to know the resource status:\n"
read -r node

# check current usage usage at the Node level and display the Pods running on the selected Node
kubectl top node --sort-by="${resource}" | egrep --color "${node}|"
echo -e "\e[0;32m Pods running on node "${node}" \e[0m"
kubectl get po -A --field-selector spec.nodeName="${node}"

### NAMESPACE LEVEL
# read namespace and pod name
echo -e "Available namespaces are:\n $(kubectl get ns -o=custom-columns=NAMESPACES:.metadata.name) \n"
echo -e "\n Please write the name of the namespace for which you want to know the resource status:\n"
read -r nspace

# most resource expensive PODS
echo -e "\e[0;32m Most ${resource}  expensive PODS in ${nspace} namespace: \e[0m"
kubectl top po -n "${nspace}" --sort-by="${resource}"
# most resource expensive CONTAINERS
echo -e "\e[0;32m Most ${resource} expensive CONTAINERS in ${nspace} namespace: \e[0m"
kubectl top po -n "${nspace}" --containers=true --sort-by="${resource}"


### POD LEVEL
echo -e "\n Please select a POD from namespace:\n $(kubectl -n "${nspace}" get po -o=custom-columns=POD:.metadata.name) \n"
read -r ppod
## check Limits and Requests for Containers in Pod and current usage
echo -e "........."
echo -e "\e[4mContainers in POD:\e[24m $(kubectl -n "${nspace}" get po "${ppod}" -o jsonpath='{.spec.containers[*].name}') \n"
echo -e "\e[4mLimits and Request per CONTAINER:\e[24m $(kubectl -n "${nspace}" get po "${ppod}" -o jsonpath='{.spec.containers[*].resources}'|jq .) \n"
echo -e "\e[4mCurrent resource usage:\e[24m\n"
kubectl -n "${nspace}" top po "${ppod}" --containers
