# Use the Alpine Linux base image
FROM alpine:latest

# Update the package repository and install OpenSSL
RUN apk update && \
    apk upgrade && \
    apk add --no-cache openssl

# Set the default command to run when the container starts
CMD ["/bin/sh"]
