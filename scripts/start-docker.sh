#!/usr//bin/bash

# mongo db
# docker run -d \
#     --network blog --network-alias mongo \
#     -v mongodb:/data/db \
#     mongo

# my blog

docker run \
    -d \
    -it \
    --network blog \
    -p 127.0.0.1:80:80 \
    myblog
