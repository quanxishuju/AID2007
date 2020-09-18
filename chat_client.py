from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ('127.0.0.1', 8000)


def login(sock):
    name = input("请输入姓名：")
    sock.sendto(name.encode(), ADDR)
    data, addr = sock.recvfrom(1024)
    if data.decode() == 'ok':
        print("您已进入聊天室")
        return   # break
    else:
        print("该用户已存在")

def main():
    sock = socket(AF_INET, SOCK_DGRAM)

    login(sock)  # 进入聊天室


if __name__ = '__main__':
    main()
