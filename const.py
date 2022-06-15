LOGO = """
  ____   ____    _    ____ ____  __________ _____ _  __
 |  _ \ / ___|  / \  |  _ \___ \|__  / ____| ____| |/ /
 | |_) | |     / _ \ | |_) |__) | / /|  _| |  _| | ' / 
 |  __/| |___ / ___ \|  __// __/ / /_| |___| |___| . \ 
 |_|    \____/_/   \_\_|  |_____/____|_____|_____|_|\_\.
 version: 0.1                                                                  
"""

DESCRIPTION = "Tool to easily and quickly convert .pcap files to Netflow format" \
              "or Zeek logs. \n" \
              "For Zeek, your settings and additional scripts can be added to the " \
              "local.zeek file. "
ZEEK_BIN_PATH = "/opt/zeek/bin/zeek" #based on linux-machine
ZEEK_SETTING_NAME = "local.zeek"

OUTPUT_FOLDER_ZEEK = "output_zeek"
OUTPUT_FOLDER_NETFLOW = "output_netflow"

TEMPORARY_FOLDER = "tmp"
