import argparse
import sys

import const
import os
import logging

import pcap2zeeklib as conv


def init():
    root = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    root.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')  # - %(name)s
    handler.setFormatter(formatter)
    root.addHandler(handler)


### For recursive to be impelmented
def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def folders(path):
    directory_contents = [f for f in os.listdir(path) if f.endswith(r".pcap")]
    logging.info(f"Found {len(directory_contents)} .pcaps in folder")
    for item in directory_contents:
        output_folder = f'{os.getcwd()}/{const.OUTPUT_FOLDER}/{item}_ZEEK'
        item_path = f'{path}/{item}'
        conv.check_output_folder(output_folder)
        conv.pcap2zeeklogs(item_path, output_folder)


def run(args):
    if args.path:
        if args.write_folder:
            conv.pcap2zeeklogs(os.path.abspath(args.path)
                               , os.path.abspath(args.write_folder))
        else:
            write_path = f'{os.getcwd()}/{const.OUTPUT_FOLDER}'
            conv.pcap2zeeklogs(os.path.abspath(args.path)
                               , write_path)
    elif args.folder:
        folders(os.path.abspath(args.folder))
    else:
        parser.print_help()


if __name__ == '__main__':
    init()

    parser = argparse.ArgumentParser(prog=const.LOGO,
                                     usage='%(prog)s [options] path',
                                     description='A script to convert to Zeek logs',
                                     )

    parser.add_argument('-p', '--path', metavar='Path to Pcap', type=str,
                        default=None,
                        help='Single pcap file')

    parser.add_argument('-f', '--folder', metavar='read folder path', type=str,
                        help='Folder path to Pcaps')

    parser.add_argument('-w', '--write_folder', metavar='write folder path', type=str,
                        help='Folder path to store, only works with single Pcap')

    # parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
    #                     help='the file where the sum should be')

    args = parser.parse_args()
    run(args)
