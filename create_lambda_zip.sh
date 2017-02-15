#!/usr/bin/env bash

path_to_app=`pwd`
path_to_libs=$path_to_app/../venv/lib/python2.7/site-packages

cd /tmp
[ -e app ] && rm -Rf app
[ -e bundle.zip ] && rm -Rf bundle.zip
mkdir app
cd app

cp -R $path_to_app/* .

rm create_lambda_zip.sh
rm requirements.txt
rm README.rst
rm setup.py
rm .gitignore
rm -Rf .idea
rm -Rf .git

zip -r9 /tmp/bundle.zip *
cd $path_to_libs
zip -r9 /tmp/bundle.zip *

# cp /tmp/bundle.zip $path_to_app

