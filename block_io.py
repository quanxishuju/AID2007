from socket import *
import time

sockfd = socket()
sockfd.bind('0.0.0.0', 6666)
sockfd.listen(5)

sockfd.setblocking(False)

while True:
    try:
        print("Waiting for connect")
        connfd, addr = sockfd.accept()
        print("Connect from:", addr)
    except BlockingIOError:
