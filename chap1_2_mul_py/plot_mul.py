import time
from mul1 import mul_nn
import matplotlib.pyplot as plt
import math
import random
from tqdm import tqdm


def main():
    x = []
    y = []
    for i in tqdm(range(11)):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))

        # 計測部
        t1 = time.time()
        mul_nn(a, b)
        t2 = time.time()

        elapsed_time = t2-t1
        x.append(math.log(keta, 2))
        y.append(elapsed_time)

    # 描画
    plt.plot(x, y, marker='^')
    plt.yscale('log')
    plt.savefig("mul.png")


if __name__ == '__main__':
    main()
