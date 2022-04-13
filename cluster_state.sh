
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

# oc adm manage-node <node1> <node2> --list-pods [--pod-selector=<pod_selector>] [-o json|yaml]

#==================================================================ALIASES

# check health Metrics API
alias kstate='kubectl get --raw "/healthz?verbose"'

# list all obj type from all namespaces, usage: ko po/svc/deployment/pv
alias ko='f(){ kubectl get $1 -A -o go-template="{{range .items}} --> {{.metadata.name}} in namespace: {{.metadata.namespace}}{{\"\n\"}}{{end}}"; unset -f f; }; f'

# check no of pods per node
alias knode_pods='kubectl get po -ojson -A | jq ".items | group_by(.spec.nodeName) | map({"nodeName": .[0].spec.nodeName, "count": length}) | sort_by(.count)"'

# check pods which are running or not
alias pods_notrunning='kubectl get pods -A --field-selector=status.phase!=Running'
alias pods_running='kubectl get pods -A --field-selector=status.phase=Running'

# check restarted pods 
alias pods_restarted='kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount!=0'

# check namespace events
alias kns_events='for n in $(kubectl get ns -o go-template="{{range .items}}{{.metadata.name}}{{\"\n\"}}{{end}}");do kubectl get events -n $n;done'

#############

# get pod just name
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'

# get pod pod/name
kubectl get po -oname -A

# get custom columns e.g. NAME columns
kubectl get po -o=custom-columns=NAME:.metadata.name -A

# get pod name with go templates are a powerful method to customize output however you want
kubectl get po -A -o go-template='{{range .items}} --> {{.metadata.name}} in namespace: {{.metadata.namespace}}{{"\n"}}{{end}}'
