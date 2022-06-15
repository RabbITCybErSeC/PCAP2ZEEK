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

Tool provides easy functionality for converting Raw packet-packet captures to Zeek logs format.

### Usage:
```
python main.py -h

optional arguments:
  -h, --help            show this help message and exit
  -p Path to Pcap, --path Path to Pcap
                        Single pcap file
  -f read folder path, --folder read folder path
                        Folder path to Pcaps
  -w write folder path, --write_folder write folder path
                        Folder path to store
```
Note that the program requires a `local.zeek` file in the same folder the `main.py` file. 

Example:
```
 python main.py -p "/home/user/dataset/attacker.pcap" -w "/home/user/ouput_folder"
```
### Requirements:
The tool requires the following dependencies:

- ```Zeek```[Installation](https://docs.zeek.org/en/master/install.html)
- ```>= Python 3.8```

### Todo:
- Add functionality for default network statistics based on predefined logs. 
- Workout folder based conversion, and recursive folder conversion. 
- Basic log anomaly detection
- Standard data visualisations. 