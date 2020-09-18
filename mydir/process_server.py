from multiprocessing import Process
from socket import *
from signal import *

# 网络地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"ok")
    connfd.close()


signal(SIGCHLD, SIG_IGN)


# 搭建并发网络
def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print('listen the port %d' % PORT)
    signal(SIGCHLD, SIG_IGN)
    # 循环等待客户端连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("服务结束")
        p = Process(target=handle, args=(connfd,))
        p.start()
