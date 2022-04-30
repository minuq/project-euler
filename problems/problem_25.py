"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""


def fib():
    idx = 0
    f1 = 1
    f2 = 1
    while (len(str(f1))<1000):
        tmp = f1+f2
        f2 = f1
        f1 = tmp
        idx += 1
    return idx

def main():
    result = fib()+2
    print("Problem 23: {0}".format(result))
