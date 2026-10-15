#!/bin/sh
# deploys straight to the production box
rsync -a . tom@brewline.co.uk:/srv/brewline && ssh tom@brewline.co.uk "cd /srv/brewline && npm i && pm2 restart brewline"
