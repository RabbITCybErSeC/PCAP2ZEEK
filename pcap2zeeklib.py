import logging
import os
import sys
import const
import subprocess


def check_zeek_settings(path):
    filename = f'{path}/{const.ZEEK_SETTING_NAME}'
    if os.path.isfile(filename):
        logging.info("Found local.zeek file for Zeek settings")
    else:
        logging.error("No Zeek settings file exists please make one!")
        sys.exit(0)
    return filename


def check_output_folder(path):
    foldername = f'{path}/{const.OUTPUT_FOLDER}'
    logging.info("Checking if output folder exists")
    if not os.path.exists(foldername):
        # Create a new directory because it does not exist
        logging.info("Output folder does not exists trying to make one")
        os.makedirs(foldername)
        logging.info("The new directory is created!")
    # print("exit")


def pcap2zeeklogs(pcap_file_name, write_path):
    cwd = os.getcwd()
    logging.info(cwd)
    zeek_path = check_zeek_settings(cwd)
    check_output_folder(write_path)
    foldername = f'{write_path}/{const.OUTPUT_FOLDER}'
    logging.info(f"Attempting Convert")
    subprocess.run([const.ZEEK_BIN_PATH, "-Cr", pcap_file_name, zeek_path],
                   cwd=foldername)
    logging.info(f"Done")
