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


def run(args):
    if args.path:
        if args.write_folder:
            print(args.write_folder)
            conv.pcap2zeeklogs(args.path, args.write_folder)
        else:
            conv.pcap2zeeklogs(args.path, os.getcwd())

    elif args.folder:
        pass
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
                        help='Folder path to store ')

    # parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
    #                     help='the file where the sum should be')

    args = parser.parse_args()
    run(args)
