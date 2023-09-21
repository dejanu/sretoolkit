# Container with openssl

* OpenSSL 3.1.3 19 Sep 2023 (Library: OpenSSL 3.1.3 19 Sep 2023)
* Start container with interactive shell:
`docker run -itu 0 dejanualex/openssl:1.0  /bin/sh`
* Start pod with interactive shell:
`kubectl  run myopenssl -i --tty --image=dejanualex/openssl:1.0  -- sh`
* Dockerhub repo [openssl](https://hub.docker.com/repository/docker/dejanualex/openssl/general)