#!/bin/bash
echo "[ERROR] Installer not tested & done yet"

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install cmake make gcc g++ flex bison libpcap-dev libssl-dev python3 python3-dev swig zlib1g-dev -y

git clone https://github.com/phaag/nfdump.git
cd nfdump

./autogen.sh
./configure --enable-sflow --enable-readpcap --enable-nfpcapd
make

sudo make install
sudo ldconfig

echo "[INFO] Cleaning up"
rm -r nfdump

echo "[INFO] Trying to install ZEEK"

echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
sudo apt update
sudo apt install zeek-lts

