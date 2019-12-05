import pandas as pd
import matplotlib.pyplot as plt
import os


def main():
    PATH = "./"
    fileNames = os.listdir(PATH)
    fileNames = [file for file in fileNames if '.csv' in file]

    plt.yscale('log')
    for fname in fileNames:
        df = pd.read_csv(PATH + fname, index_col=0)
        print(fname)
        plt.plot(df, marker='^', label=fname)
    plt.legend()
    plt.title("mul compare")
    plt.xlabel("n : 2 ** x")
    plt.ylabel("sec")
    plt.savefig("compare.png")


if __name__ == '__main__':
    main()
