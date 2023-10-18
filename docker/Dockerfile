FROM ubuntu:14.04
COPY test.txt .
# Install cowsay
RUN apt-get update && apt-get install -y cowsay --no-install-recommends
# "cowsay" installs to /usr/games
ENV PATH $PATH:/usr/games
CMD ["cowsay","Hello World!"]
