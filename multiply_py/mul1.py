import random


def mul_2(l, m):
    ans = (l * m)
    return ans // 10, ans % 10


def add(l, m):
    ans = (l + m)
    return ans // 10, ans % 10


def add_3(l, m, n):
    ans = (l + m + n)
    return ans // 10, ans % 10


def mul1(a, b):
    # print(a * b)
    a = list(map(int, list(str(a))))[::-1]
    ans = [0] * (len(a) + 1)
    carry = 0
    prev_c = 0
    for i in range(len(a)):
        c, d = mul_2(a[i], b)
        carry, tmp = add_3(d, prev_c, carry)
        ans[i] = tmp
        prev_c = c
    ans[-1] = prev_c + carry
    ans = ans[::-1]
    # print(ans)
    # print(int("".join(list(map(str, ans)))))
    return ans


def mul_nn(a, b):
    inta = a
    a = list(map(int, list(str(a))))[::-1]
    b = list(map(int, list(str(b))))[::-1]
    if len(b) > len(a):
        a, b = b, a
    ans = [0] * (len(a) + len(b) + 1)

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

