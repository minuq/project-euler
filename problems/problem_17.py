oneToTen = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
            10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
            100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred',
            600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred', 1000: 'one thousand'}


def calc(n):
    # print(n)
    try:
        # print(oneToTen[n])
        return (oneToTen[n]).replace(' ', '')
    except KeyError:
        if n > 100:
            # print(n - n % 100, n % 100)
            # print(str(calc(n - n % 100)) + ' and ' + str(calc(n % 100)))
            return str(calc(n - n % 100)) + ' and ' + str(calc(n % 100))
        else:
            # print(n - n % 10, n % 10)
            # print(str(calc(n - n % 10)) + str(calc(n % 10)))
            return str(calc(n - n % 10)) + str(calc(n % 10))


def main():
    result = 0
    for x in range(1, 1001):
        # print(calc(x))
        result += len(calc(x).replace(' ', ''))
    print(result)
