import logging
import os
import const
import subprocess


def check_output_folder(path):
    logging.info("Checking if output folder exists")
    if not os.path.exists(path):
        # Create a new directory because it does not exist
        logging.info("Output folder does not exists trying to make one")
        os.makedirs(path)
        logging.info("The new directory is created!")
    # print("exit")


def remove_tmp_folder(tmp_folder):
    for file in os.scandir(tmp_folder):
        os.remove(file.path)
    os.rmdir(tmp_folder)
    logging.info(f"Done")


def pcap2netflowV5(pcap_file_name, write_path):
    cwd = os.getcwd()
    tmp_folder = f'{cwd}/{const.TEMPORARY_FOLDER}'
    check_output_folder(write_path)
    logging.info(f"Attempting Convert for: {pcap_file_name}")
    logging.info(f"Making temporary folder for NFdump format")

    check_output_folder(tmp_folder)
    subprocess.run(["nfpcapd", "-r", pcap_file_name, "-l", tmp_folder])

    # nfdump/bin/nfdump -R /path/to/dir/with/capdfiles
    # nfdump -r <nflow_file> -o extended -o csv > <output_file>

    my_cmd = ["nfdump", "-R", tmp_folder, "-o", "extended", "-o", "csv", ]
    output_file_name = pcap_file_name.split("/")[-1]

    with open(f'{write_path}/{output_file_name}.csv', "w") as outfile:
        subprocess.run(my_cmd, stdout=outfile)
    logging.info(f"Attempting to remove temporary folder")
    remove_tmp_folder(tmp_folder)
