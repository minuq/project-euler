def collatz(arr, num):
    if num == 1:
        return arr
    if num % 2 == 0:
        arr.append(num)
        return collatz(arr, int(num/2))
    if num % 2 != 0:
        arr.append(num)
        return collatz(arr, int(num * 3 + 1))
    print(arr)


def main():
    result = 0
    length = 0
    i = 2
    arr = []
    while i < 1000000:
        arr = []
        tmp = collatz(arr, i)
        if len(tmp) > length:
            length = len(tmp)
            result = i
        i += 1
    # print(arr)
    print("Problem 14: {0}".format(result))
