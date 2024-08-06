import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def circle_area(radius):
    return math.pi * (radius ** 2)

def circle_circumference(radius):
    return 2 * math.pi * radius

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c
