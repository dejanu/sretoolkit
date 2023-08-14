### Start web-server as standalone :

```bash
flask run --host=0.0.0.0 --port=8080
```

### Build it:
```bash
docker build -t dejanualex/opensslapp:1.0 .
sudo docker run -p 8080:8080 --rm --name certapp dejanualex/opensslapp:1.0
```