import time
from karatsuba import karatsuba_nn
import matplotlib.pyplot as plt
import math
import random
from tqdm import tqdm
import pandas as pd
from utils import to_ls


def pl_karatsuba(reps, n0):
    x = []
    y = []
    for i in tqdm(range(reps)):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        a = to_ls(a)
        b = to_ls(b)
        # 計測部
        t1 = time.time()
        karatsuba_nn(a, b, n0)
        t2 = time.time()

        elapsed_time = t2-t1
        x.append(math.log(keta, 2))
        y.append(elapsed_time)

    # 描画
    plt.plot(x, y, marker='^')
    plt.yscale('log')
    plt.savefig("karatsuba.png")
    df = pd.DataFrame({'2**': x, 'time': y})
    df.to_csv("karatsuba_{}.csv".format(n0), index=False)


if __name__ == '__main__':
    pl_karatsuba(13, 4)
    pl_karatsuba(13, 32)
