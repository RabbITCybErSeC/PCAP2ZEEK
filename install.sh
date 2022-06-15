#!/bin/bash
echo "[ERROR] Installer not test & done yet"


exit 0

sudo apt-get install flex
sudo apt-get install libpcap-dev

git clone https://github.com/phaag/nfdump.git
cd nfdump
chmod u+x autogen.sh && ./autogen.sh
./configure --enable-sflow --enable-readpcap --enable-nfpcapd
make
sudo make install
