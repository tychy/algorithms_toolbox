from utils import int_ls, to_ls


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

    for i in range(len(b), len(a)):
        carry, tmp = add_3(a[i], prev_c, carry)
        ans[i] = tmp
        prev_c = 0
    ans[-1] = carry
    ans = ans[::-1]
    # print(int("".join(list(map(str, ans)))))

    return ans


if __name__ == '__main__':
    a = 123850
    b = 123856
    a = to_ls(a)
    b = to_ls(b)
    add_nn(a, b)
