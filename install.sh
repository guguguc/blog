#!/usr/bin/bash

# install docker
apt update && apt install docker.io

# install docker-compose
curl \
    -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

touch /var/log/nginx/access.log
touch /var/log/nginx/error.log

docker-compose up -d
