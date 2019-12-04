import time
from mul1 import mul1
import matplotlib.pyplot as plt
import math
import random
from utils import to_ls


def main():
    x = []
    y = []
    for i in range(14):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randint(1, 10)
        a = to_ls(a)
        b = b
        # 計測部
        t1 = time.time()
        mul1(a, b)
        t2 = time.time()

        elapsed_time = t2-t1
        x.append(math.log(keta, 2))
        y.append(elapsed_time)

    # 描画
    plt.plot(x, y, marker='^')
    plt.yscale('log')
    plt.savefig("mul1.png")


if __name__ == '__main__':
    main()
