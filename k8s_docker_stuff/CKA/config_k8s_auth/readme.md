## General info

* There are two categories of users in Kubernetes: normal users and service accounts.
*  Kubernetes supports authentication using:
```
x509 certificates
Bearer tokens
Basic authentication (usernames and passwords)
OpenID Connect (OIDC) tokens (currently limited support)
```

* User `andy` with cert

```bash
mkdir certs  # create certificate directory
sudo openssl genrsa -out certs/andy.key 2048  # generate private key
sudo chmod 666 certs/andy.key  # make the key read & write
```

```bash
# allow OpenSSL to create a certificate signing request (CSR) for the user Andy
sudo sed -i 's%RANDFILE.*=.*$ENV::HOME/.rnd%#RANDFILE = $ENV::HOME/.rnd%' /etc/ssl/openssl.cnf
# create a cert signing request CSR for user Andy  member of the network-admin group:
openssl req -new -key certs/andy.key -out certs/andy.csr -subj "/CN=andy/O=network-admin"

# Common names (/CN) are mapped to the name of users
# Organizations (/O) are mapped to the name of groups
```

* Create a k8s certificate signing requests

```yaml

apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: new-user-request
spec:
  signerName: kubernetes.io/kube-apiserver-client
  request: $(cat certs/andy.csr | base64 | tr -d '\n')
  usages:
  - digital signature
  - key encipherment
  - client auth
```

* Approve the CSR

```bash
kubectl certificate approve new-user-request
```