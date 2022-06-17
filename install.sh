#!/bin/bash

echo "[INFO] Installer might be buggy please report \n"

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

echo "[INFO] Trying to install ZEEK \n"

. /etc/os-release

echo -n "[INFO] Detected Ubuntu version: $VERSION_ID \n"

case $VERSION_ID in

  22.04)

    echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
    curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
    ;;

  21.10)
    echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_21.10/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
    curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_21.10/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
    ;;

  20.04)
    echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
    curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
    ;;

  18.04)
    echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_18.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
    curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_18.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
    ;;
esac

sudo apt update
sudo apt install zeek-lts

