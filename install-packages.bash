#!/bin/bash
yum -y update

# install selenium
easy_install pip
pip install selenium

# install Xvfb and firefox
yum -y install xorg-x11-server-Xvfb firefox

# install drivers

# Gecko driver
wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
tar xvzf geckodriver-v0.17.0-linux64.tar.gz geckodriver
chown root:root geckodriver
mv geckodriver /usr/local/bin

# PhantomJS driver
yum -y install fontconfig freetype freetype-devel fontconfig-devel libstdc++
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
mkdir -p /opt/phantomjs
mv phantomjs-2.1.1-linux-x86_64.tar.bz2 /opt/phantomjs
cd /opt/phantomjs
tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 --strip-components 1

# install Django
yum -y install epel-release
yum -y install python-django
