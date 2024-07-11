year = 2023
divisible_by_4 = (year % 4 == 0)


if divisible_by_4:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f"{year} is a leap year: yes")
else:
    print(f"{year} is a leap year: No")