def main():
    result = calc()
    print("Problem 10: {0}".format(result))


def calc():
    arr = prime(200000)
    result = 0
    for i in arr:
        result += i
    return result


def prime(n):
    primes = [2]
    num = 3
    while num < n:
        tmp = True
        for i in primes:
            if num % i == 0:
                tmp = False
                break
        if tmp:
            primes.append(num)

        # if num % 10000 == 1:
        #    print(num)
        num += 2
    return primes

