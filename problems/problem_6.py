def main():
    print(summation(100)-multiplication(100))


def summation(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res*res


def multiplication(n):
    res = 0
    for i in range(1, n+1):
        res += i * i
    return res
