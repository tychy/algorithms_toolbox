from mul1 import mul_nn
import random
from tqdm import tqdm


def main():
    for i in tqdm(range(10)):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        ans = mul_nn(a, b)
        true_checksum = ((a % 9) * (b % 9)) % 9
        calc_checksum = int("".join(list(map(str, ans)))) % 9
        print(true_checksum == calc_checksum)


if __name__ == '__main__':
    main()
