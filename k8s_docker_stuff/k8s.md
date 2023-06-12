### Control plane checks:
```bash
# get control plane status
kubectl get cs
kubectl get componentstatuses

# get version k8s
kubectl version --short

# apiserver endpoints
#echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/healthz?verbose')" # deprecated v1.16
echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/livez?verbose')"
echo -e "\e[0;32m Status of APIs Server: \e[0m \n $(kubectl get --raw '/readyz?verbose')"
```

### Customize output:
```bash
kubectl get po -o=custom-columns=NAME:.metadata.name -A
# Go templates are a powerful method to customize output however you want
kubectl get po -A -o go-template='{{range .items}} --> {{.metadata.name}} in namespace: {{.metadata.namespace}}{{"\n"}}{{end}}'
kubectl get po -o name -A

#k8s objects: po,rs,svc,deployments
kubectl get pods -A (--all-namespaces )
kubectl get pods --show-labels
kubectl get pods -w (--watch)
kubectl get pods -o json
```
### Go templates
```bash
# use custom columns
kubectl get ns -o=custom-columns=NAMESPACE_NAME:.metadata.name
kubectl get po -o=custom-columns=POD_NAME:.metadata.name
```
