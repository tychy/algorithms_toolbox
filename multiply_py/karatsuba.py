import random
from mul1 import add, add_3, mul_2, mul1, mul_nn
from add import add_nn


def karatsuba_nn(a, b, n0):
    inta = a
    a = list(map(int, list(str(a))))[::-1]
    b = list(map(int, list(str(b))))[::-1]
    if len(b) > len(a):
        a, b = b, a
    if len(b) <= n0:
        return int_ls(mul_nn(a, b))
    k = len(a) // 2
    ans = [0] * (len(a) + len(b) + 1)
    a0 = a[:k]
    a1 = a[k:]
    b0 = b[:k]
    b1 = b[k:]



    for i in range(len(b)):
        p = mul1(inta, b[i])
        p = p[::-1]  # p : len(a) + 1
        carry = 0
        for j in range(i, i + len(a) + 1):
            carry, d = add_3(ans[j], carry, p[j - i])
            ans[j] = d
        if carry > 0:
            ans[i + len(a) + 1] = ans[i + len(a) + 1] + carry
            # out of bound　にならないことは保証されているはず
    ans = ans[::-1]
    # print(int("".join(list(map(str, ans)))))
    return ans


if __name__ == '__main__':
    a = 993850
    b = 901
    mul_nn(a, b)

    for i in range(14):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        # print(a * b)
        # print(mul_nn(a, b))
        print((a * b) == mul_nn(a, b))
