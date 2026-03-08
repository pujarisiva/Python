import sys
import os

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])


if operation == "addition":
    output = addition(num1, num2)
    print(output)

elif operation == "subtraction":
    output = subtraction(num1, num2)
    print(output)

elif operation == "multiplication":
    output = multiplication(num1, num2)
    print(output)

else:
    print("Invalid operation")

print(os.getenv("password"))    