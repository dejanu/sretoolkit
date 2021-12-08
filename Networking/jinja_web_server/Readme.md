# Usage:
```bash

docker build -t dejanualex/lbapp:1.0 .
sudo docker run -p 9095:9095 --rm --name lbapp -e "LB_URL=https://new_url" dejanualex/lbapp:1.0
```
