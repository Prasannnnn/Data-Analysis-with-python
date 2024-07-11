# Let's take a year to check
year_to_check = 2024

# First, we need to check if the year can be divided by 4
divisible_by_4 = (year_to_check % 4 == 0)

# But, if the year can also be divided by 100, then it's not a leap year
# except if it can also be divided by 400
if divisible_by_4:
    if year_to_check % 100 == 0:
        if year_to_check % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

# Now let's print the result
if is_leap_year:
    print(f"{year_to_check} is a leap year: Yes")
else:
    print(f"{year_to_check} is a leap year: No")
