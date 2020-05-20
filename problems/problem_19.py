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
    print(day, month, year)
    res = 0
    for i in range(1, month, 1):
        res += daysinmonth(i, year)
    res += day
    return res


def daysinmonth(month, leap):
    feb = 28
    if leap:
        feb = 29
    return {
        1: 31,
        2: feb,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }.get(month)


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
    # for i in range(1900, 1920, 1):
    #    print(i, daysinyear(i))
    # for j in range(1, 12, 1):
    #    print(j, daysinmonth(j, False), daysinmonth(j, True))
    print(dayofyear(31, 12, 1990))
    result = daysinyear(1999)
    print("Problem 19: {0}".format(result))
