def calendar(year):
    is_leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    else:
        is_leap = False
    return is_leap
