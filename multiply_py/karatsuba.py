import random
from mul1 import mul_nn
from add import add_nn
from sub import sub_nn
from utils import int_ls, to_ls


def karatsuba_nn(a_ls, b_ls, n0=4):
    if len(b_ls) > len(a_ls):
        a_ls, b_ls = b_ls, a_ls
    if len(b_ls) <= n0:
        return mul_nn(a_ls, b_ls)
    k = len(a_ls) // 2
    a0 = a_ls[:k]
    a1 = a_ls[k:]
    b0 = b_ls[:k]
    b1 = b_ls[k:]
    a1pa0 = add_nn(a1, a0)
    b1pb0 = add_nn(b1, b0)
    p1 = karatsuba_nn(a1pa0, b1pb0, n0)
    p2 = karatsuba_nn(a1, b1, n0)
    p0 = karatsuba_nn(a0, b0, n0)
    p0pp2 = add_nn(p0, p2)
    p1sp0pp1 = sub_nn(p1, p0pp2)
    pright2 = add_nn(p1sp0pp1, p0[k:])
    ans = p0[:k] + pright2[:k] + add_nn(p2, pright2[k:])
    return ans


if __name__ == '__main__':
    a = 76732
    b = 70600
    a = to_ls(a)
    b = to_ls(b)
    karatsuba_nn(a, b)
    for i in range(10000):
        keta = 15 # 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        a = to_ls(a)
        b = to_ls(b)
        # print(int_ls(a) * int_ls(b))
        # print(int_ls(mul_nn(a, b)))
        # print(int_ls(karatsuba_nn(a, b)))
        # print((int_ls(a) * int_ls(b)) == int_ls(karatsuba_nn(a, b)))
        if not ((int_ls(a) * int_ls(b)) == int_ls(karatsuba_nn(a, b))):
            print(int_ls(a))
            print(int_ls(b))

