from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST, PORT)


# 框架 启动函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 循环等待接收请求
    while True:
        # 所有请求都在这接收
        data, addr = sock.recvfrom(1024)
        print(data.decode())
        # 根据请求选择功能
        if data == "进入":
            pass
        elif data == '聊天': 
            pass


if __name__ == '__main__':
    main()
