#!/usr/bin/env python3

def admin_login(username, password):
    """
    Return "Access granted" if username is "admin" (case-insensitive) and password is "12345";
    otherwise return "Access denied".
    """
    # Normalize username to lowercase for comparison
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"


def hows_the_weather(temp):
    """
    Return a weather comment based on the temperature:
    - below 40: "It's brisk out there!"
    - 40 to 65: "It's a little chilly out there!"
    - above 85: "It's too dang hot out there!"
    - otherwise: "It's perfect out there!"
    """
    if temp < 40:
        return "It's brisk out there!"
    elif 40 <= temp <= 65:
        return "It's a little chilly out there!"
    elif temp > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(n):
    """
    Return "Fizz" if n is a multiple of 3,
    "Buzz" if n is a multiple of 5,
    "FizzBuzz" if n is a multiple of both 3 and 5,
    otherwise return the number itself.
    """
    # Multiples of both 3 and 5 first
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


def calculator(operation, a, b):
    """
    Perform basic arithmetic operations:
    +, -, *, /. If operation is invalid, print an error and return None.
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        # handle division by zero gracefully
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None
