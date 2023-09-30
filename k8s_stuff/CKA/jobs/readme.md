
# Usage

While most API objects are deployed such that they continue to be available there are some which we may want to run a
particular number of times called a **Job**, and others on a regular basis called a **CronJob**.

* Job = creates one or more Pods and will continue to retry execution of the Pods until a specified number of them successfully terminate. As pods successfully complete, the Job tracks the successful completions

* [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) = creates a watch loop which will create a batch job on your behalf when the time becomes true.

```bash
# job = sort of task, k8s will schedule a job and it will run it once and it will not be rescheduled - 1 time, when u apply it it gets executed and that's it aka init container

# cronjob = a job that runs on a schedule
```

## Example

* Delete failed helm release

```bash
# these are hr k8s object that can be deployed by argo or flux
kubectl get hr -A

# these are deployed with helm
helm list -A -o json | jq -r '.[].name'

# create job
kubectl apply -f job_helm.yaml
kubectl logs jobs/helmclean
```

## RBAC

* Permissions are granted to a ServiceAccount
```bash
# check api resources and verbs
kubectl api-resources -owide
```
* ServiceAccount --> Role (rules for API groups) --> RoleBinding (binds role to service account or user)



