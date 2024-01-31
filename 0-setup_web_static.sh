#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
apt-get update -y
apt-get install nginx -y
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "www.hamzed.tech" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
