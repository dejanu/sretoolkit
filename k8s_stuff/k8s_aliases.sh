#!/usr/bin/env bash

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
alias pods_restarted='kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount'

# check namespace events
alias kns_events='for n in $(kubectl get ns -o go-template="{{range .items}}{{.metadata.name}}{{\"\n\"}}{{end}}");do kubectl get events -n $n;done'

# check vault status
alias vaultstatus='kubectl -n vault exec vault-0 -- vault status'

#############

# get pod just name
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'

# get pod pod/name
kubectl get po -oname -A

# get custom columns e.g. NAME columns
kubectl get po -o=custom-columns=NAME:.metadata.name -A

# get pod name with go templates are a powerful method to customize output however you want
kubectl get po -A -o go-template='{{range .items}} --> {{.metadata.name}} in namespace: {{.metadata.namespace}}{{"\n"}}{{end}}'