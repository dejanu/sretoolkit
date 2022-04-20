#!/usr/bin/env bash

# include aliases by adding this line: [ -f $HOME/.k8s_aliases ] && . $HOME/.k8s_aliases and copying this file in $HOME location

__usage="
Aliases:
  kstate -  get cluster health
  ko <object> - list all <object> type from all namespaces
  knode_pods - list pods node allocation
  kpods_runnig - list all running pods from all namespaces
  kpods_completed - list all completed pods from all namespaces
  kpods_notrunnig - list all NOT running pods from all namespaces e.g: CrashLoopBackOff
  kpods_restarted - sort restarted pods
  kns_events - list events from each namespace
  vaultstatus - check vault status
"
echo "$__usage"
# enable auto-completion
source <(kubectl completion bash)
# check health Metrics API
alias kstate='kubectl get --raw "/healthz?verbose"'
# list all obj type from all namespaces, usage: ko po/svc/deployment/pv/rs/hr
alias ko='f(){ kubectl get $1 -A -o go-template="{{range .items}} --> {{.metadata.name}} in namespace: {{.metadata.namespace}}{{\"\n\"}}{{end}}"; unset -f f; }; f'
# check no of pods per node
alias knode_pods='kubectl get nodes && kubectl get po -ojson -A | jq ".items | group_by(.spec.nodeName) | map({"nodeName": .[0].spec.nodeName, "count": length}) | sort_by(.count)"'
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