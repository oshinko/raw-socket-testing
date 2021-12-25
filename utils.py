import fcntl
import socket
import struct


def macaddr(interface):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        arg = struct.pack('256s', interface.encode('utf8')[:15])
        info = fcntl.ioctl(sock.fileno(), 0x8927, arg)
        return info[18:24]
