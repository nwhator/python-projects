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


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiation")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

choice = input("Enter your choice (1 - 10): ")

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
elif choice == '8':
    if result is None:
        num = float(input("Enter the angle in degrees: "))
    else:
        num = result
    result = sine(num)
    print("Sine of", num, "=", round(result, 4))
elif choice == '9':
    if result is None:
        num = float(input("Enter the angle in degrees: "))
    else:
        num = result
    result = cosine(num)
    print("Cosine of", num, "=", round(result, 4))
elif choice == '10':
    if result is None:
        num = float(input("Enter the angle in degrees: "))
    else:
        num = result
    result = tangent(num)
    print("Tangent of", num, "=", round(result, 4))
else:
    print("Wrong input. Please choose a number from 1 to 10.")
