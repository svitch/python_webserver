#!/usr/bin/env bash
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/sergey/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
