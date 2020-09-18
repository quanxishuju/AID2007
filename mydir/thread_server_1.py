from threading import Thread
from socket import *
import sys

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        connfd, addr = sock.accept()
        p = Thread(target=handle,args=(connfd,))
        p.start()