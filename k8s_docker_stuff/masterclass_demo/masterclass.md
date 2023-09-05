# Setup with kubectl

* kubectl tool supports verb-driven commands for creating some of the most common object types.

```bash
# create a resource from a file or STDIN
kubectl create -f FILENAME

# create a deployment with 2 pods running nginx
kubectl create deployment webapp --image=nginx:1.17.8 --replicas=2 --dry-run=client -o yaml

kubectl create deployment webapp --image=nginx:1.17.8 --replicas=2 -oyaml > first_deployment.yaml

# create service object which serves on port 80 (container port) and connects to the containers on port 8000(pod port)
kubectl expose deploy webapp --name=webapp-svc --type="ClusterIP" --port=8080 --target-port=80 # ngnix default port is 80

# curl the service from within the cluster
kubectl get svc webapp-svc -o yaml | grep clusterIP
curl 10.103.36.137:8080

# kubectl edit  trigger a rolling update
kubectl edit deploy webapp

# view object revisions
kubectl rollout history deploy <deployment>
```