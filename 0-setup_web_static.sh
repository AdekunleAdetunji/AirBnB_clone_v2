#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# install nginx
if ! (nginx -v)
then
    apt-get update -y
    apt-get install -y nginx
fi

# create the desired directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create an html index page containing the content of the idx_cont variable
idx_cont="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$idx_cont" | tee /data/web_static/releases/test/index.html > /dev/null

# pcreate a symbolic link to current to the test directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of the /data/ folder to the ubuntu user AND group
chown --recursive "$USER":"$USER" /data

# configure nginx to serve the index of /data/web_static/current when hbnb_static/ dir is queried
sedStr="\\
\tlocation /hbnb_static {\\
\t\t alias /data/web_static/current/;\\
\t}"
sed -i '/server_name _;/a '"$sedStr"'' /etc/nginx/sites-enabled/default

# restart nginx
service nginx restart
