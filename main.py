import argparse
import sys

import const
import os
import logging

import pcap2zeeklib as zeekconv
import pcap2netflowlib as netflowconv


def init():
    root = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    root.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')  # - %(name)s
    handler.setFormatter(formatter)
    root.addHandler(handler)


# ### For recursive to be impelmented
# def fast_scandir(dirname):
#     subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
#     for dirname in list(subfolders):
#         subfolders.extend(fast_scandir(dirname))
#     return subfolders

def folders_conversion_zeek(path):
    directory_contents = [f for f in os.listdir(path) if f.endswith(r".pcap")]
    logging.info(f"Found {len(directory_contents)} .pcaps in folder")
    for item in directory_contents:
        output_folder = f'{os.getcwd()}/{const.OUTPUT_FOLDER_ZEEK}/{item}_ZEEK'
        item_path = f'{path}/{item}'
        zeekconv.check_output_folder(output_folder)
        zeekconv.pcap2zeeklogs(item_path, output_folder)


def folder_conversion_netflow(path):
    directory_contents = [f for f in os.listdir(path) if f.endswith(r".pcap")]
    logging.info(f"Found {len(directory_contents)} .pcaps in folder")
    for item in directory_contents:
        output_folder = f'{os.getcwd()}/{const.OUTPUT_FOLDER_NETFLOW}/'
        item_path = f'{path}/{item}'
        netflowconv.check_output_folder(output_folder)
        netflowconv.pcap2netflowV5(item_path, output_folder)


def run(args):
    if args.zeek:
        if args.path:
            if args.write_folder:
                zeekconv.pcap2zeeklogs(os.path.abspath(args.path)
                                       , os.path.abspath(args.write_folder))
            else:
                write_path = f'{os.getcwd()}/{const.OUTPUT_FOLDER_ZEEK}'
                zeekconv.pcap2zeeklogs(os.path.abspath(args.path)
                                       , write_path)
        elif args.folder:
            folders_conversion_zeek(os.path.abspath(args.folder))
        else:
            parser.print_help()

    elif args.netflow:
        if args.path:
            write_path = f'{os.getcwd()}/{const.OUTPUT_FOLDER_NETFLOW}'
            netflowconv.pcap2netflowV5(os.path.abspath(args.path)
                                       , write_path)

            if args.write_folder:
                netflowconv.pcap2netflowV5(os.path.abspath(args.path)
                                           , os.path.abspath(args.write_folder))
            else:
                write_path = f'{os.getcwd()}/{const.OUTPUT_FOLDER_NETFLOW}'
                netflowconv.pcap2netflowV5(os.path.abspath(args.path)
                                           , write_path)
        elif args.folder:
            folder_conversion_netflow(os.path.abspath(args.folder))
        else:
            parser.print_help()
    else:
        parser.print_help()


if __name__ == '__main__':
    init()

    parser = argparse.ArgumentParser(prog=const.LOGO,
                                     description=const.DESCRIPTION,
                                     )
    parser.add_argument('-n', '--netflow', help="Flag for exporting as netflow format", action='store_true')
    parser.add_argument('-z', '--zeek', help="Flag for exporting as Zeek format", action='store_true')
    parser.add_argument('-p', '--path', metavar='<path>', type=str,
                        default=None,
                        help='Single pcap file')

    parser.add_argument('-f', '--folder', metavar='<path>', type=str,
                        help='Folder path to Pcaps')

    parser.add_argument('-w', '--write_folder', metavar='<path>', type=str,
                        help='Folder path to store, only works with single Pcap')

    # parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
    #                     help='the file where the sum should be')

    args = parser.parse_args()
    run(args)
