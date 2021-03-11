#!/bin/sh

nginx && uwsgi -i scripts/uwsgi.ini -d /var/log/uwsgi/blog.log
/bin/sh
