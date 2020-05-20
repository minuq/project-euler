def main():
    print(calc(20))


def calc(n):
    res = 0
    tmp = True
    while tmp:
        tmp = False
        res += 1
        for i in range(1, n):
            # print(res % i, res, i, tmp)
            if res % i != 0:
                tmp = True
    return res
