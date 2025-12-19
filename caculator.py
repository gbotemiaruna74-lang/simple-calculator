def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! cannot divide by zero."
    return a / b

print("Welcome to ab's caculator")
print("choose op: +,-,*,/")

num1 = float(input("enter number:  "))
num2 = float(input("enter number: "))
op = input("Enter op (+,-,*,/): ")

if op == "+":
    print("Result", add(num1, num2))
elif op == "-":
    print("Result", subtract(num1, num2))
elif op == "*":
    print("Result", multiply(num1, num2))
elif op == "/":
    print("Result", divide(num1, num2))
else:
    print("Invalid  operation")