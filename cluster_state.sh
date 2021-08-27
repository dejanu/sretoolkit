
#!/usr/bin/bash

# reviewing cluster node health status as cluster-admin role

oc logout 2>/dev/null
echo "Select cluster ***********"
echo " 1) OKD 4.7 cluster:"
echo " 2) OKD 3.x cluster:"
read n
case $n in
        1) oc login --username=<USER> --password=<PASSWORD> --insecure-skip-tls-verify --server=<CLUSTER> && oc cluster-info;;
        2) oc login --username=<USER> --password=<PASSWORD> --insecure-skip-tls-verify --server=<CLUSTER> && oc cluster-info;;
esac

# list all nodes known to master: 
oc version && oc get nodes

echo -e "======================= \033[0;33mSorted Events at NODE level\e[0m================="
#oc get events --sort-by='{.lastTimestamp}' --all-namespaces -o json | jq '.items[] | select(.involvedObject.kind == "Node")'|grep --color -i failed
oc get events --sort-by='{.lastTimestamp}' --all-namespaces -o json | jq '.items[] | select(.involvedObject.kind == "Node")'| grep --color -Ei "host|message"
#echo "=======================Sorted Events at POD level================="
#oc get events --sort-by='{.lastTimestamp}' --all-namespaces -o json | jq '.items[] | select(.involvedObject.kind == "Pod")'|grep -E 'message|name'
echo -e "======================= \033[0;33mUsage Stats\e[0m================="
# CPU and memory usage for each node
oc adm top nodes --use-protocol-buffers
for i in $(oc get nodes | awk 'FNR>1 {print $1}');do echo -e "Allocated resources \033[1;4;32;41mNode $i: \e[0m";oc describe node $i| awk -v RS=':' '/Addresses/';done
echo "Start debug pod for a node: oc debug node/<NODE_NAME>"
