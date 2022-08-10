- kubelet is daemon on each worked node, managed by  systemd (journalctl -u kubelet) or if it's mangaged by upstart (logs are here /var/log/upstart).
- k8s scheduler assignes a POD to a NODE, then the kubelet reads the POD specs and instructs  (using CRI) the container runtime to spin-up 
the containers that satisfy that spec

- kubelet can register the node with the apiserver using one of: the hostname; a flag to override the hostname; or specific logic for a cloud provider.

- control plane components: etcd, controller, scheduler, kube-proxy, core-dns, network plugin (those pods should be running to be sure that Kubernetes is healthy)


- Non-Graceful Node Shutdown [graceful shutdown  only if the node shutdown action can be detected by the kubelet (daemon on each worker node) ahead of the actual shutdown]

- Node Non-Graceful == node shutdown action takes place without the kubelet daemon (on each worker node) knwoing about it => pods on that node also shut down ungracefully.

- https://www.containiq.com/post/kubernetes-events