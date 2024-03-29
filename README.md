```
  ____   ____    _    ____ ____  __________ _____ _  __
 |  _ \ / ___|  / \  |  _ \___ \|__  / ____| ____| |/ /
 | |_) | |     / _ \ | |_) |__) | / /|  _| |  _| | ' /
 |  __/| |___ / ___ \|  __// __/ / /_| |___| |___| . \
 |_|    \____/_/   \_\_|  |_____/____|_____|_____|_|\_\
 version: 0.1
```

## PCAP2Zeek Tool

### Description:
Tool to easily and quickly convert .pcap files to Netflow format or Zeek logs.
For Zeek, your settings and additional scripts can be added to the local.zeek file.

### Installer:
Note that the installer is only made for Ubuntu. 
```
git clone https://github.com/thehoodbuddha/PCAP2ZEEK.git
sudo apt-get update && upgrade -y
cd PCAP2ZEEK
sudo chmod +x install.sh
./install.sh
```
### Usage:
```
python main.py -h

options:
  -h, --help            show this help message and exit
  -n, --netflow         Flag for exporting as netflow format
  -z, --zeek            Flag for exporting as Zeek format
  -p <path>, --path <path>
                        Single pcap file
  -f <path>, --folder <path>
                        Folder path to Pcaps
  -w <path>, --write_folder <path>
                        Folder path to store, only works with single Pcap

```
Note that the program requires a `local.zeek` file in the same folder the `main.py` file. 
Conversion to Netflow format is based on the method proposed by [markelic](https://markelic.de/how-to-get-netflow-from-a-pcap-file/) 
& [jjsantanna](https://gist.github.com/jjsantanna/f2ee2f1fe23208299f4a2ca392f8b23f?permalink_comment_id=3540601)

Example:
```
 python main.py -z -p "/home/user/dataset/attacker.pcap" -w "/home/user/ouput_folder"
```
```
 python main.py -n -f "/home/user/dataset"
```

### Alternative Tools:
- Python NetFlow/IPFIX library [Github](https://github.com/bitkeks/python-netflow-v9-softflowd)
### Requirements:
The tool requires the following dependencies:

- ```Zeek```[Installation](https://docs.zeek.org/en/master/install.html)
- ```nfdump & nfpcapd```[nfdump & nfpcapd](https://github.com/phaag/nfdump)
- ```>= Python 3.8```

Note: Tool only has been tested on debian based system. 


Note: (“nfpcapd: is the pcap capture daemon of the nfdump tools.
It reads network packets from an interface or from a file and directly creates nfdump netflow records.”
from https://github.com/phaag/nfdump/blob/master/man/nfpcapd.1

### Todo:
- Auto tool installer in under development
- Add functionality for default network statistics based on predefined logs. 
- Workout folder based conversion, and recursive folder conversion. 
- Basic log anomaly detection
- Standard data visualisations. 