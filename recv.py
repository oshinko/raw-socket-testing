import argparse
import datetime
import pathlib
import socket

import utils

ETH_P_ALL = 3

parser = argparse.ArgumentParser(pathlib.Path(__file__).name)
parser.add_argument('--interface', required=True)
parser.add_argument('--ether-type', type=bytes.fromhex, default=b'\x88\xb5')

args = parser.parse_args()

proto = socket.htons(ETH_P_ALL)

with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, proto) as sock:
    sock.bind((args.interface, 0))
    n = 0

    me = utils.macaddr(args.interface)

    while True:
        data = sock.recv(1514)
        to = data[:6]
        ether_type = data[12:14]
        payload = data[14:]

        n += 1
        t = datetime.datetime.now().isoformat()

        if to != me or ether_type != args.ether_type:
            continue

        try:
            payload = payload.decode('utf8')
        except UnicodeDecodeError:
            # print(n, t, ether_type.hex(), end='\n\n')
            pass

        print(n, t, ether_type.hex(), payload, end='\n\n')
