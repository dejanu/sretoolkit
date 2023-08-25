FROM alpine:latest

# Install necessary dependencies
RUN apk --no-cache add bash curl

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/
    
# Copy your script
COPY helmrelease_status.sh /helmrelease_status.sh
RUN chmod +x /helmrelease_status.sh

