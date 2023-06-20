# Docker stuff

```bash
# docker stats
docker system info
docker ps --format 'table {{.Names}}\t{{.Status}}'
docker system df

## Debug Docker
sudo systemctl status docker
sudo journalctl -xeu docker.service
journalctl -u docker
sudo systemctl daemon-reload

# get events
docker events --filter event=restart --since=60m
docker events --filter event=restart --since=60m > events.log 2>&1
## service vs systemctl
service docker restart
systemctl start docker

systemctl daemon-reload
systemctl stop docker
systemctl start docker
```