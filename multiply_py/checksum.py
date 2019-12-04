from mul1 import mul_nn
import random
from tqdm import tqdm
from utils import to_ls, int_ls


def main():
    for i in tqdm(range(10)):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        a = to_ls(a)
        b = to_ls(b)
        ans = mul_nn(a, b)
        true_checksum = ((int_ls(a) % 9) * (int_ls(b) % 9)) % 9
        calc_checksum = int_ls(ans) % 9
        print(true_checksum == calc_checksum)


if __name__ == '__main__':
    main()
