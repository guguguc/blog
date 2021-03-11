FROM alpine:latest

WORKDIR /usr/src/blog
EXPOSE 80

# sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' \
# /etc/apk/repositories \

RUN apk update \
    && apk add --no-cache \
    python3 \
    py3-pip \
    uwsgi-python3 \
    nginx \
    vim

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /run/nginx \
    && cp scripts/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["/bin/sh", "scripts/start.sh"]
