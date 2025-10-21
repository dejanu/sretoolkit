* A Pod in the mcp namespace has a single container named random that writes its logs to the /var/log/random.log file. Add a second container named second that uses the busybox image to allow the following command to display the logs written to the random container's /var/log/random.log file:

```bash
# kubectl log po container
kubectl -n mcp logs random second
```

* Solution:

```yaml

apiVersion: v1
kind: Pod
metadata:
  name: random
  namespace: mcp
spec:
  containers:
  - args:
    - /bin/sh
    - -c
    - while true; do shuf -i 0-1 -n 1 >> /var/log/random.log; sleep 1; done
    image: busybox
    name: random
    volumeMounts:
    - mountPath: /var/log
      name: logs
  - name: second
    image: busybox
    args: [/bin/sh, -c, 'tail -n+1 -f /var/log/random.log']
    volumeMounts:
    - name: logs
      mountPath: /var/log
  volumes:
  - name: logs
    emptyDir: {}

```

- Link sidecar container: https://kubernetes.io/docs/concepts/cluster-administration/logging/#sidecar-container-with-logging-agent