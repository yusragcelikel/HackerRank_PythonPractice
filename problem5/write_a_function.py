def is_leap(year):
    leap = False

    if year % 100 == 0:
        year = year / 100
        if year % 4 != 0:
            leap
        else:
            leap = True
    elif year % 4 == 0:
        leap = True

    return leap


year = int(input())
print(is_leap(year))