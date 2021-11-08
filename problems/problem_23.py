"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def d(num):
    res = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            res.append(i)
    return sum(res)

def isAbundant(num):
    res = False
    if d(num) > num:
        res = True
    return res

def expressed(abundants,limit):
    res = []
    for i in range(0,limit+1):
        res.append(i)
    for i in range (0,len(abundants)):
        for j in range(i,len(abundants)):
            tmp = abundants[i]+abundants[j]
            if tmp > 28123:
                continue
            res[tmp]= 0
    return sum(res)

def main():
    abundants = []
    result = 0
    limit = 28123
    for i in range(1,limit):
        if isAbundant(i):
            abundants.append(i)
    result = expressed(abundants,limit)
    print("Problem 20: {0}".format(result))
