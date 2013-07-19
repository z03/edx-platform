#!/usr/bin/env bash

# Install all the requirements for running the
# acceptance test suite and the JavaScript
# unit test suite.
# 
# Requires 32-bit Ubuntu

# Exit if any commands return a non-zero status
set -e

sudo apt-get update

sudo apt-get install unzip

# Install xvfb
echo "Installing Xvfb..."
sudo apt-get install -y xvfb

# Install the xvfb upstart script
sudo cat > /etc/init/xvfb.conf <<END
description     "Xvfb X Server"
start on (net-device-up
          and local-filesystems
          and runlevel [2345])
stop on runlevel [016]
exec /usr/bin/Xvfb :99 -screen 0 1024x768x24
END

cat >> .bashrc <<END

# Set the display to the virtual frame buffer (Xvfb)
export DISPLAY=:99
END

sudo start xvfb

# Install Chrome
echo "Downloading Google Chrome..."
wget --quiet https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
sudo dpkg -i google-chrome*.deb 2> /dev/null || true
sudo apt-get -f -y install

# Install ChromeDriver
echo "Installing ChromeDriver..."
wget --quiet http://chromedriver.googlecode.com/files/chromedriver_linux32_26.0.1383.0.zip
unzip chromedriver_linux32_26.0.1383.0.zip
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chmod go+rx /usr/local/bin/chromedriver

# Install Firefox
sudo apt-get -y install firefox

# Install phantomjs
echo "Installing PhantomJS..."
wget --quiet "https://phantomjs.googlecode.com/files/phantomjs-1.9.1-linux-i686.tar.bz2"
tar -xjf phantomjs-1.9.1-linux-i686.tar.bz2
sudo mv phantomjs-1.9.1-linux-i686/bin/phantomjs /usr/local/bin/phantomjs

exit 0
