"""What is the sum of the digits of the number 2^1000?  """


def main():
    bignum = 1
    result = 0
    for i in range(0, 1000):
        bignum *= 2
    for i in range(0, len(str(bignum))):
        result += int(str(bignum)[i])
    print("Problem 16: {0}".format(result))
