def odd_number(number):
    return number % 2 !=0

def even_number(number):
    return number % 2 == 0

number = 4

if odd_number(number):
    print(f"{number} is odd number")
else:
    print(f"{number} is even number")