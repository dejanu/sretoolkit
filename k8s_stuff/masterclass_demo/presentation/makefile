.DEFAULT_GOAL := documentation

documentation:
	@echo "make imperative"
	@echo "make declarative"
	@echo "make flex"


flex:
	@echo "kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes" | jq .items[].usage"

declarative:
	@echo "kubectl applyf -f deployment.yaml"
imperative:
	@echo "kubectl create deployment nginx-imperative --image=nginx:1.17.8 --replicas=2 --dry-run=client -oyaml"
