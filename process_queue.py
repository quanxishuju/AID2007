from multiprocessing import Process, Queue

q = Queue()


def request():
    name = "Levi"
    passwd = "123"
    # 存入消息队列
    q.put(name)
    q.put(passwd)


def handle():
    name = q.get()
    passwd = q.get()
    print("用户名：", name)
    print("密码：", passwd)


p1 = Process(target=request)
p2 = Process(target=handle)

p1.start()
p2.start()

p1.join()
p2.join()
