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


def dayssincebeginning(day, month, year):
    res = 0
    leapyear = leap(year)
    # only counts complete years
    for i in range(1900, year, 1):
        res += daysinyear(i)
    for i in range(1, month, 1):
        res += daysinmonth(i, leapyear)
    res += day-1
    return res  # returns the amount of days since 1.1.1900


def dayofyear(day, month, year):
    print(day, month, year)
    res = 0
    for i in range(1, month, 1):
        res += daysinmonth(i, year)
    res += day
    return res  # returns how many days have passed since the beginning of a year


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
    }.get(month)  # returns how many days are in a given month depending on leapyear status


def weekdayStr(days):
    return {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }.get(days % 7+1)


def weekday(days):
    return days % 7 + 1


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
    # print(dayssincebeginning(1, 1, 1900), 0)  # 0
    # print(dayssincebeginning(2, 1, 1900), 1)  # 1
    # print(dayssincebeginning(1, 2, 1900), 31)  # 31
    # print(dayssincebeginning(1, 1, 2000), 365)  # 365
    # day = 20
    # month = 5
    # year = 2020
    # result = weekday(dayssincebeginning(day, month, year))
    result = 0
    for i in range(1901, 2001, 1):
        for j in range(1, 13, 1):
            if (weekday(dayssincebeginning(1, j, i)) == 7):  # 1. day of month j in year i
                result += 1
    print("Problem 19: {0}".format(result))
