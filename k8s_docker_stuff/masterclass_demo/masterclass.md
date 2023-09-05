# Setup with kubectl

* kubectl tool supports verb-driven commands for creating some of the most common object types.

```bash
# create a resource from a file or STDIN
kubectl create -f FILENAME

# create a deployment with 2 pods running nginx
kubectl create deployment webapp --image=nginx:1.17.8 --replicas=2 --dry-run=client -oyaml

kubectl create deployment webapp --image=nginx:1.17.8 --replicas=2 -oyaml > first_deployment.yaml

# create service object which serves on port 80 (container port) and connects to the containers on port 8000(pod port)
kubectl expose deploy webapp --name=webapp-svc --type="ClusterIP" --port=8080 --target-port=80 # ngnix default port is 80

# curl the service from within the cluster
kubectl get svc webapp-svc -o yaml | grep clusterIP
curl 10.103.36.137:8080

# spin-up a pod with curl and busybox and curl from it: curl 10.103.36.137:8080
kubectl run client --image=radial/busyboxplus:curl -i --tty --rm
kubectl run client --image=appropriate/curl -it --rm --restart=Never -- sh

# change the service type to LoadBalancer
kubectl patch svc webapp-svc -p '{"spec": {"type": "LoadBalancer"}}'

# kubectl edit  trigger a rolling update
kubectl edit deploy webapp

# view object revisions
kubectl rollout history deploy <deployment>
```


## Links:

* [tips and tricks](https://www.ibm.com/blog/8-kubernetes-tips-and-tricks/)
* [tips and triks2](https://github.com/yokawasa/kubectl-tips)

## Official docs:

* [kubectl getting started](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-strong-getting-started-strong-)
* [kubectl cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)



https://kubernetes.io/training/
https://kubernetes.io/docs/reference/
