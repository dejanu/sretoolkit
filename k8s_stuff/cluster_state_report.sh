#!/usr/bin/env bash

################################################################################################
# kubectl wrapper that generates a report concerning cluster state,                           ##
# which creates a dir with compiled information regarding:                                    ##
#  - control plane components status, cluster events, nodes description, and namespace events ##                        
################################################################################################

# Get nodes, componentsstatuses, and pods for control-plane
echo -e "\e[0;32m Cluster Nodes: \e[0m \n $(kubectl get nodes -owide)"
echo -e "\e[0;32m Cluster State: \e[0m \n $(kubectl get cs)"
echo -e "\e[0;32m Control Plane: \e[0m \n $(kubectl get pods -owide -n kube-system | grep kube-apiserver)"

# apiserver endpoints
#echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/healthz?verbose')" # deprecated v1.16
echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/livez?verbose')"
echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/readyz?verbose')"

# dumps from kube-system namespace
REPORT_NAME=cluster_report_$(date +%Y%m%d_%H%M%S)_$(kubectl config current-context)
mkdir -p $REPORT_NAME
kubectl cluster-info dump --output-directory=$REPORT_NAME

# get sorted event objects from all namespaces
kubectl get events --sort-by='.metadata.creationTimestamp' -A > $REPORT_NAME/cluster_events.txt
# kubectl get events --sort-by='{.lastTimestamp}' -A -ojson| jq '.items[] | select(.involvedObject.kind == "Pod")' | tee $REPORT_NAME/pod_events.txt

# storage state
tee $REPORT_NAME/storage_state.txt > /dev/null <<EOF
CSI drivers installed nodes:
---------------------------
$(kubectl get csinodes)
$(kubectl get storageclasses)
Cluster Volume attachments:
---------------------------
$(kubectl get volumeattachments)
EOF

# extracting cluster nodes info
for no in $(kubectl get nodes -o=custom-columns=NAME:.metadata.name -A | awk '(NR>1)'); do
   kubectl describe node $no > $REPORT_NAME/$no.txt  
done

echo -e "\e[0;32m Report generated -> $REPORT_NAME \e[0m"