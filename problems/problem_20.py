"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def quersumme(n):
    quer = str(n)
    tmp = 0
    for i in range(0,len(quer)):
        tmp += int(quer[i])
        i+=1
    return tmp

def factorial(n):
    tmp = 1
    for i in range(1,n):
        tmp *= i
    return tmp

def main():
    result = quersumme(factorial(100))
    print("Problem 20: {0}".format(result))
