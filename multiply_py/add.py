from utils import int_ls, to_ls
import random

def add(l, m):
    ans = (l + m)
    return ans // 10, ans % 10


def add_3(l, m, n):
    ans = (l + m + n)
    return ans // 10, ans % 10


def add_nn(a, b):
    # print(a + b)
    if len(b) > len(a):
        a, b = b, a
    ans = [0] * (len(a) + 1)
    carry = 0
    prev_c = 0
    for i in range(len(b)):
        c, d = add(a[i], b[i])
        carry, tmp = add_3(d, prev_c, carry)
        ans[i] = tmp
        prev_c = c
    carry = prev_c + carry
    prev_c = 0
    for i in range(len(b), len(a)):
        carry, tmp = add_3(a[i], prev_c, carry)
        ans[i] = tmp
        prev_c = 0
    ans[-1] = carry
    # print(int("".join(list(map(str, ans)))))
    while ans[-1] == 0 and len(ans) > 1:
        ans.pop()
    return ans


if __name__ == '__main__':
    for i in range(8):
        keta = 5 # 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        a = to_ls(a)
        b = to_ls(b)
        # print(int_ls(a) + int_ls(b))
        # print(int_ls(add_nn(a, b)))
        print((int_ls(a) + int_ls(b)) == int_ls(add_nn(a, b)))
