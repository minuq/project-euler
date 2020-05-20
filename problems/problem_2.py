def fib(n):
    if n == 1:
        return 1
    return n + fib(n-1)


def main():
    n = 0
    m = 1
    result = 0
    while n < 4000000:
        tmp = n
        n = n + m
        m = tmp
        if n % 2 == 0:
            result += n
        # print(n, n % 2)
    # print(n, result)
    print("Problem 2:", result)
