
# start jenkins and ignore hangup

 nohup java -jar jenkins.war --httpPort=-1 --httpsPort=9443 --httpsKeyStore="/path/to/certstore.jks" --httpsKeyStorePassword=[PASSWORD] > nohup.out 2>&1 &
 
 # plugins .hpi and script console
 
 println(hudson.util.Secret.decrypt("{HASH=}")) OR println(hudson.util.Secret.fromString("{XXX= HASH}").getPlainText())
 println(hudson.util.Secret.fromString("some_text").getEncryptedValue())



# For more information on running Jenkins on Kubernetes, visit:
# https://cloud.google.com/solutions/jenkins-on-container-engine
# add chart repo <REPO_NAME> has been added to your repositories
helm repo add <REPO_NAME>  https://artifactory/<REPO_NAME>  --username USER --password PASSWORD
 
#pick the latest chart version
helm upgrade -i <release_name> <REPO_NAME>  /<CHART> --version 2.12

#search in repo
helm repo list
helm repo update
helm search repo <CHART> --versions

# Get your 'admin' user password by running
printf $(kubectl get secret --namespace NAMESPACE -o <RELEASE-CHART> -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo

oc login

oc rollout status deploy o <RELEASE-CHART>
oc get route o <RELEASE-CHART> -o jsonpath="{.status.ingress[0].host}"
oc rollout status deploy <depoyment_name>

 
