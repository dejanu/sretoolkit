# Deploying ingress

* [ingress nginx](https://github.com/kubernetes/ingress-nginx/blob/main/docs/deploy/index.md)



```bash
kubectl get ingress -A

# add helm repo
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm search hub ingress

# download the chart
helm fetch ingress-nginx/ingress-nginx --untar
helm install myingress ./ingress-nginx

```