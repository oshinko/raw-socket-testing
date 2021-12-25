import argparse
import pathlib
import socket

import utils

ETH_P_ALL = 3

parser = argparse.ArgumentParser(pathlib.Path(__file__).name)
parser.add_argument('--interface', required=True)
parser.add_argument('--to', type=bytes.fromhex, required=True)
parser.add_argument('--ether-type', type=bytes.fromhex, default=b'\x88\xb5')
parser.add_argument('payload', type=str)

args = parser.parse_args()

proto = socket.htons(ETH_P_ALL)

with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, proto) as sock:
  sock.bind((args.interface, 0))
  me = utils.macaddr(args.interface)
  sock.sendall(args.to + me + args.ether_type + args.payload.encode('utf8'))
  print('Sent!')
