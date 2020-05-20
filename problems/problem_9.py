def main():
    result = calc()
    print("Problem 9: {0}".format(result))


def sqr(n):
    return n * n


def calc():
    a = 1
    b = 2
    c = 3
    while c < 998:
        b = 2
        while b < c:
            a = 1
            while a < b:
                # print(a, b, c)
                if sqr(a) + sqr(b) == sqr(c):
                    if a + b + c == 1000:
                        return a * b * c
                a += 1
            b += 1
        c += 1
