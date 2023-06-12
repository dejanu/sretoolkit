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
sudodocker

## service vs systemctl
service docker restart
systemctl start docker

systemctl daemon-reload
systemctl stop docker
systemctl start docker
```