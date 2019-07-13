# Set the base image to Ubuntu
FROM ubuntu:16.04



# Install basics
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python && \
    apt-get install -y wget \
    curl \
    bc \
    unzip \
    less \
    bedtools \
    samtools \
    openjdk-8-jdk \
    tabix \
    bwa\
    python-pip\
    software-properties-common && \
    apt-get -y clean  && \
    apt-get -y autoclean  && \
    apt-get -y autoremove

#Create and set the dir for you script
RUN mkdir -p /usr/src/app

WORKDIR /usr/srv/app

#Copy requirements and script
COPY . /usr/srv/app

#Install python dependecies
RUN pip install -r requirements.txt


# CMD ["python","./myscript.py"]
CMD ["/bin/bash"]
