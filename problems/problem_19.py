"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def dayofyear(day, month, year):
    return 0


def weekday(day):
    return 0


def leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            return False
        return True
    return False


def daysinyear(year):
    if (leap(year)):
        return 366
    return 365


def main():
    for i in range(1900, 1920, 1):
        print(i, daysinyear(i))
    result = daysinyear(1999)
    print("Problem 19: {0}".format(result))
