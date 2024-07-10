num = float(input("Enter the number: "))

if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")


num = float(input("Enter the number: "))

if num % 2 == 0 and num >= 6 and num <= 20:
    print("Not Weird")
elif num % 2 == 0 and num >= 20:
    print("weird Greater")
else:
    print("Weird")