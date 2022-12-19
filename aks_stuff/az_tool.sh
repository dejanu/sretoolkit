#!/usr/bin/env bash

############################################################################
## SRE-Azure Tool wrapper                                                 ##
##                                                                        ##     
############################################################################

# check if azure cli is installed
if ! [ -x "$(command -v az)" ]; then
    echo "Azure CLI is not installed. Please install it first: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest"
    # install az cli
fi

# check if user is logged in azure cli
if [ -z "$(az account show)" ]; then
    echo "Please login to azure cli"
    az login --use-device-code
else
    echo "Logged in to azure cli with the following account:"
    az account show -o table
fi

separator_stuff="\e[1;32m ===================================================================\e[0m\n"
# list available subscriptions
echo -e "$separator_stuff Available subscriptions:"
az account list -o table --all

# select and set subscription using subscription_id variable
echo -e "$separator_stuff Select subscriptionId (e.g. 5a4600a1-a6ac-4b56-8364-00fbbd81f5de) :"
read subscription_id
az account set --subscription $subscription_id

# list all resource groups in the selected subscription
echo -e "$separator_stuff Available RESOURCE GROUPS in the selected subscription:"
#az group list -o table --query "[?contains(id, '$subscription_id')]"
az group list -o table

# select and set resource group using resource_group variable
echo -e "$separator_stuff Select resource group :"
read resource_group
echo -e "$separator_stuff Available RESOURCES in the $resource_group RESOURCE GROUP:"
az resource list --query "[?resourceGroup=='$resource_group']" -o table

# details of Azure resource consumption as an invoice for the selected resource 
#az consumption usage list --subscription "$subscription_id" --query "[].{Name:instanceName, Product:product, Usage:usageQuantity}" -o table
echo -e "$separator_stuff Azure consumption for Selected Subscription and  RESOURCE GROUP:"
az consumption budget list --subscription "$subscription_id" -o table
az consumption budget list -g '$resource_group' -o table
