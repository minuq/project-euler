import math


def main():
    # number to test 600851475143
    # 13195
    primes = prime(10000)
    primefactors = []
    calc(600851475143, primes, primefactors)
    # print(primefactors)
    print("Problem 3:", max(primefactors))


def calc(n, primes, primefactors):
    for x in primes:
        # print(x)
        if n % x == 0 and int(n / x) != 1:
            # print(n, "%", x, "==", 0)
            # print(n, "/", x, "==", int(n/x))
            primefactors.append(x)
            return calc(int(n / x), primes, primefactors)
        if n % x == 0 and int(n / x) == 1:
            # print(n, "is a prime")
            primefactors.append(n)
            return n


def prime2(n):
    primes = []
    for x in range(2, n):
        primes.append(x)
    # print(primes)
    # print(primes[int(len(primes) / 2)])
    for i in primes:
        x = 0
        while x < len(primes):
            # print(primes, x, primes[x], i)
            if primes[x] % i == 0 and int(primes[x] / i) != 1:
                primes.pop(x)
            x += 1
    return primes


def prime(n):
    primes = [2]
    num = 2
    while len(primes) < n:
        tmp = True
        for i in primes:
            if num % i == 0:
                tmp = False
                break
        if tmp:
            primes.append(num)
        # print(primes)
        num += 1
    return primes
