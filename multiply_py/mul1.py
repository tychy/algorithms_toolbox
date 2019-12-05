import random
from utils import int_ls, to_ls


def mul_2(l, m):
    ans = (l * m)
    return ans // 10, ans % 10


def add(l, m):
    ans = (l + m)
    return ans // 10, ans % 10


def add_3(l, m, n):
    ans = (l + m + n)
    return ans // 10, ans % 10


def mul1(a_ls, b):
    # print(a * b)
    ans = [0] * (len(a_ls) + 1)
    carry = 0
    prev_c = 0
    for i in range(len(a_ls)):
        c, d = mul_2(a_ls[i], b)
        carry, tmp = add_3(d, prev_c, carry)
        ans[i] = tmp
        prev_c = c
    ans[-1] = prev_c + carry
    # print(ans)
    # print(int("".join(list(map(str, ans)))))
    return ans


def mul_nn(a_ls, b_ls):
    if len(b_ls) > len(a_ls):
        a_ls, b_ls = b_ls, a_ls
    ans = [0] * (len(a_ls) + len(b_ls) + 1)

    for i in range(len(b_ls)):
        p = mul1(a_ls, b_ls[i])
        p = p  # p : len(a) + 1
        carry = 0
        for j in range(i, i + len(a_ls) + 1):
            carry, d = add_3(ans[j], carry, p[j - i])
            ans[j] = d
        if carry > 0:
            ans[i + len(a_ls) + 1] = ans[i + len(a_ls) + 1] + carry
            # out of bound　にならないことは保証されているはず
    # print(int("".join(list(map(str, ans)))))

    # while ans[-1] == 0 and len(ans) > 1:
    #   ans.pop()
    return ans


if __name__ == '__main__':
    """
    a = 9930033500
    b = 9023510
    a = to_ls(a)
    b = to_ls(b)
    print(int_ls(a) * int_ls(b))
    print(int_ls(mul_nn(a, b)))
    print((int_ls(a) * int_ls(b)) == int_ls(mul_nn(a, b)))
    """
    for i in range(8):
        keta = 8 * (2**i)
        a = random.randrange(10 ** keta, 10 ** (keta + 1))
        b = random.randrange(10 ** keta, 10 ** (keta + 1))
        a = to_ls(a)
        b = to_ls(b)
        print(int_ls(a) * int_ls(b))
        print(int_ls(mul_nn(a, b)))
        print((int_ls(a) * int_ls(b)) == int_ls(mul_nn(a, b)))
