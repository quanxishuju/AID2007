from multiprocessing import Process


class MyProcess:
    def __init(self, value):
        self.value = value
        super().__init__()

    def fun(self):
        print("今天周六")

    def run(self):
        self.run()
        print("明天周日")
p = MyProcess()
p.start()
