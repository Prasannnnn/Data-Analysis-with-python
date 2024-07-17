def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b


def floor(a,b):
    return a//b


def mod(a,b):
    return a%b


a = float(input("Enter the a Value: "))
b = float(input("Enter the b Value: "))
print("Enter the operator of add, sub, mult, div, floor and mod")
operator = input("Enter the operator")

if operator == "add":
    print(f"the addition of {a} and {b} is {add(a,b)}")