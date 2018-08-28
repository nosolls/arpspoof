#!/bin/sh

node wetty/app.js -p 3000 && \
/usr/sbin/apachectl -D FOREGROUND 

