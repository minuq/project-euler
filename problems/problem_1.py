"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def problem(n):
    result = 0
    for i in range(0, 1000, n):
        result = result+i
    return result


def main():
    print("Problem 1:", problem(3)+problem(5)-problem(15))
