def factors(num, length):
    """
    Sped up greatly by assuming that for a number to be divisible by n numbers, there's gotta be at least n/5
    factors in the first n natural numbers, which prove true
    :param num: current triangle to test
    :param length: maximum length of the array
    :return: number of factors
    """
    cnt = 1
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            cnt += 1
        if i > length and cnt < int(length/5):
            return cnt
    return cnt


def main():
    result = 0
    length = 600
    tmp = 0
    triangle = 0
    while result < length:
        tmp += 1
        triangle += tmp
        tmp2 = factors(triangle, length)
        if tmp2 > result:
            result = tmp2
        print(triangle, "+", tmp, result, end="\r")

    print("Problem 12: {0} has {1} divisors".format(triangle, result))
