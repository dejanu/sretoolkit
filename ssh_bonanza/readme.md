# Oneline to run cmd/script on multiple hosts using ssh

```bash
# the servers list reside in the servers.txt file
while read -u10 line;do echo $line;ssh ansible@$line 'bash -s' < script_remote_ssh.sh;done 10< servers.txt
while read -u10 line;do ssh $line 'docker-compose --version';done 10<servers.txt
```



