#!/usr/bin/env bash

# include aliases by adding this line: [ -f $HOME/.k8s_aliases ] && . $HOME/.k8s_aliases and copying this file in $HOME location 

__usage="
\e[1;33m Aliases:\e[0m
  \e[0;32m kstate \e[0m   -  get cluster health 
  \e[0;32m kns_events \e[0m - list events from each namespace,pretty verbose
  \e[0;32m ko <object> \e[0m - list all <object> type from all namespace
  \e[0;32m knodes \e[0m - list cluster nodes name
  \e[0;32m knode_pods \e[0m - sorted list of pods node allocation
  \e[0;32m knode_status_pods <node_name> \e[0m - pods status with regard to a certain node
  \e[0;32m kpods_running \e[0m - list all running pods from all namespaces
  \e[0;32m kpods_notrunning \e[0m - list all NOT running pods from all namespaces e.g: CrashLoopBackOff
  \e[0;32m kpods_completed \e[0m - list all completed pods from all namespaces
  \e[0;32m kpods_restarted \e[0m - sort restarted pods
  \e[0;32m vaultstatus \e[0m - check vault status
"
echo -e "$__usage"
# enable auto-completion
source <(kubectl completion bash)
# check health Metrics API
alias kstate='kubectl get --raw "/healthz?verbose"'

# list nodes
alias knodes='kubectl get nodes -oname'
# check no of pods per node
alias knode_pods='kubectl get nodes && kubectl get po -ojson -A | jq ".items | group_by(.spec.nodeName) | map({"nodeName": .[0].spec.nodeName, "count": length}) | sort_by(.count)"'
# pods status with regard to a certain node
#alias knode_status_pods='f(){ kubectl get po -A -owide --field-selector spec.nodeName=$1; unset -f f; }; f'
alias knode_status_pods='f(){ kubectl get po -A --field-selector spec.nodeName=$1; unset -f f; }; f'

# list all obj type from all namespaces, usage: ko po/svc/deployment/pv/rs/hr
alias ko='f(){ kubectl get $1 -A -o go-template="{{range .items}} --> {{.metadata.name}} in NAMESPACE: {{.metadata.namespace}}{{\"\n\"}}{{end}}"; unset -f f; }; f'

# check pods which are running or not
alias kpods_completed='kubectl get pods -A --field-selector=status.phase!=Running' #shows Completed
#alias kpods_notrunning='kubectl get po -A -ocustom-columns=NAMESPACE:metadata.namespace,POD:metadata.name,PodIP:status.podIP,STATE:status.containerStatuses[*].state.waiting.reason|grep CrashLoopBackOff'
alias kpods_notrunning='kubectl get po -A|grep -E "ImagePullBackOff|CrashLoopBackOff"'
alias kpods_running='kubectl get pods -A --field-selector=status.phase=Running'
alias kpods_restarted='kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount'

# check namespace events
alias kns_events='for n in $(kubectl get ns -o go-template="{{range .items}}{{.metadata.name}}{{\"\n\"}}{{end}}");do kubectl get events -n $n;done'
# check vault status
alias vaultstatus='kubectl get po -n vault&&kubectl -n vault exec vault-0 -- vault status'

function kubectlgetall {
  for i in $(kubectl api-resources --verbs=list --namespaced -o name | grep -v "events.events.k8s.io" | grep -v "events" | sort | uniq); do
    echo "Resource:" $i
    kubectl -n ${1} get --ignore-not-found ${i}
  done
}