import time
from add import add_nn
import matplotlib.pyplot as plt
import math
import random


def main():
    x = []
    y = []
    for i in range(14):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))

        # 計測部
        t1 = time.time()
        add_nn(a, b)
        t2 = time.time()

        elapsed_time = t2-t1
        x.append(math.log(keta, 2))
        y.append(elapsed_time)

    # 描画
    plt.plot(x, y, marker='^')
    plt.yscale('log')
    plt.savefig("add.png")


if __name__ == '__main__':
    main()
