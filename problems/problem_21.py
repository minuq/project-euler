"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(num):
    res = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            res.append(i)
    return sum(res)


def main():
    arr = []
    res = 0
    tmp = 0
    while tmp < 10000:
        pair1 = d(tmp)
        pair2 = d(pair1)
        if tmp == pair2 and pair1 != pair2:
            if [min(pair1,pair2),max(pair1,pair2)] not in arr:
                arr.append([min(pair1,pair2),max(pair1,pair2)])
                res += pair1+pair2
        tmp += 1
    print("Problem 20: {0}".format(res))
