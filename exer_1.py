from multiprocessing import Process
import time


def timeis(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("执行时间:", end_time - start_time)
        return res

    return wrapper


# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


@timeis
def compute_1():
    prime = []
    for i in range(25000):
        if isPrime(i):
            prime.append(i)
    print(sum(prime))  # 求和


@timeis
def compute_1():
    prime = []
    for i in range(25000):
        if isPrime(i):
            prime.append(i)
    print(sum(prime))  # 求和
