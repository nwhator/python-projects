#!/usr/bin/python3

import math


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def exp(x, y):
    return x ** y


def square_root(x):
    return math.sqrt(x)


def logarithm(x, base):
    return math.log(x, base)


print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiation")
print("6. Square Root")
print("7. Logarithm")

choice = input("Enter your choice (1-7): ")

result = None

if choice in ['1', '2', '3', '4']:
    if result is None:
        num1 = float(input("Enter the first number: "))
    else:
        num1 = result
    num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = sub(num1, num2)
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = mul(num1, num2)
    print(num1, "*", num2, "=", result)
elif choice == '4':
    result = div(num1, num2)
    print(num1, "/", num2, "=", result)
elif choice == '5':
    if result is None:
        num1 = float(input("Enter the number base: "))
    else:
        num1 = reult
    num2 = float(input("Enter the exponent: "))
    result = exp(num1, num2)
    print(num1, "^", num2, "=", result)
elif choice == '6':
    if result is None:
        num = float(input("Enter the number: "))
    else:
        num = result
    result = square_root(num)
    print("Square root of", num, "=", result)
elif choice == '7':
    if result is None:
        num = float(input("Enter the number: "))
    else:
        num = result
    base = float(input("Enter the logarithm base: "))
    result = logarithm(num, base)
    print("Logarithm of", num, "with base", base, "=", result)
else:
    print("Wrong input. Please choose a number from 1 to 7.")
