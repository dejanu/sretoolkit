* The following multi-container Pod manifest needs to be updated BEFORE being deployed. Container c2 is designed to make HTTP requests to container c1. Before deploying this manifest, update it by substituting the <REPLACE_HOST_HERE> placeholder with the correct host or IP address - the remaining parts of the manifest must remain unchanged. Once deployed - confirm that the solution works correctly by executing the command kubectl logs -n app1 webpod -c c2 > /home/ubuntu/webpod-log.txt. The resulting /home/ubuntu/webpod-log.txt file should contain a single string within it.


- Manifest

```yaml
apiVersion: v1
kind: Pod
metadata:
 name: webpod
 namespace: app1
spec:
 restartPolicy: Never
 volumes:
 - name: vol1
   emptyDir: {}
 containers:
 - name: c1
   image: nginx
   volumeMounts:
   - name: vol1
     mountPath: /usr/share/nginx/html
   lifecycle:
     postStart:
       exec:
         command:
           - "bash"
           - "-c"
           - |
             date | sha256sum | tr -d " *-" > /usr/share/nginx/html/index.html
 - name: c2
   image: appropriate/curl
   # HERE
   command: ["/bin/sh", "-c", "curl -s http://<REPLACE_HOST_HERE> && sleep 3600"]
```

- Solution: Containers within the same Pod share the same Pod IP address, and can communicate via loopback network interface - therefore any of the following values can be used for the <REPLACE_HOST_HERE> placeholder

```bash
* localhost
* 127.0.0.1
* webpod
* <pod.assigned.ip.address>
* <pod-assigned-ip-address>.<namespace>.pod.cluster.local
```

```yaml
# Update and deploy the provided manifest using localhost for <REPLACE_HOST_HERE>
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
 name: webpod
 namespace: app1
spec:
 restartPolicy: Never
 volumes:
 - name: vol1
   emptyDir: {}
 containers:
 - name: c1
   image: nginx
   volumeMounts:
   - name: vol1
     mountPath: /usr/share/nginx/html
   lifecycle:
     postStart:
       exec:
         command:
           - "bash"
           - "-c"
           - |
             date | sha256sum | tr -d " *-" > /usr/share/nginx/html/index.html
 - name: c2
   image: appropriate/curl
   command: ["/bin/sh", "-c", "curl -s http://localhost && sleep 3600"]
EOF
# Confirm that the pod is up and running
kubectl get pod -n app1 webpod
# Confirm that container c2 is correctly working (able to communicate with container c1)
kubectl logs -n app1 webpod -c c2
# Write out the log result for c2 to the /home/ubuntu/webpod-log.txt file
kubectl logs -n app1 webpod -c c2 > /home/ubuntu/webpod-log.txt


```