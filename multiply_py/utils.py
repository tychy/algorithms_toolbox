def int_ls(a):
    return int("".join(list(map(str, a))))


def to_ls(a):
    return list(map(int, list(str(a))))[::-1]