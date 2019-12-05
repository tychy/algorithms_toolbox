import time
from mul1 import mul_nn
import matplotlib.pyplot as plt
import math
import random
from tqdm import tqdm
import pandas as pd
from utils import to_ls, int_ls

def pl_mul(reps):
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
        int_ls(a) * int_ls(b)
        t2 = time.time()

        elapsed_time = t2-t1
        x.append(math.log(keta, 2))
        y.append(elapsed_time)

    # 描画
    plt.plot(x, y, marker='^')
    plt.yscale('log')
    plt.savefig("builtin.png")
    df = pd.DataFrame({'2**': x, 'time': y})
    df.to_csv("builtin.csv", index=False)


if __name__ == '__main__':
    pl_mul(13)
