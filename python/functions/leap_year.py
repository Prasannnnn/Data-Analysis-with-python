def leap(year):
    if (year % 4 == 0 and year % 100 == 0 ) or year % 400 != 0:
        return True
    return False

year = 2023

if leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is a non-leap year")