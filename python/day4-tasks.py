a = float(input("Enter the value of a : "))
b = float(input("Enter the Value of b : "))
c = input("Enter the operator: ")
if c == "+":
    print(f"the addition value of {a}and {b} is {a+b}")
elif c == "*":
    print(f"the multiplication value of {a} and {b} is {a*b}")
else:
    print(f"{c} is an invalid Operator")