def palindrome(n):
    x = 0
    word = str(n)
    while x < len(word)/2:
        if word[x] != word[len(word)-1-x]:
            return False
        else:
            x += 1
    return True


def calc(n):
    tmppalindrome = 0
    x = n
    while n/2 < x <= n:
        y = n
        while n/2 < y <= n:
            tmp = x * y
            if palindrome(tmp) and tmp > tmppalindrome:
                tmppalindrome = tmp
            y -= 1
        x -= 1
    return tmppalindrome


def main():
    print("Problem 4:", calc(1000))
