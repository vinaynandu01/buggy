# buggy_script.py

import os, sys

def greet_user(name)
    print("Hello, " + name)

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

def divide_numbers(a, b):
    return a / b  # Potential ZeroDivisionError

class Person
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
    print("Hi, my name is", se# buggy_script.py

import os, sys

def greet_user(name)
    print("Hello, " + name)

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

def divide_numbers(a, b):
    return a / b  # Potential ZeroDivisionError

class Person
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
    print("Hi, my name is", self.name)

# Logic error: wrong variable used
def add_numbers(x, y):
    result = x - y
    return result

if __name__ == "__main__":
    greet_user("Alice"

    r = "5"  # Should be a number, not a string
    print("Area of circle:", calculate_area(r))

    print("Division result:", divide_numbers(10, 0))

    p = Person("Bob", 30)
    p.say_hi()

    print("Sum is:", add_numbers(10, 5))
lf.name)

# Logic error: wrong variable used
def add_numbers(x, y):
    result = x - y
    return result

if __name__ == "__main__":
    greet_user("Alice"

    r = "5"  # Should be a number, not a string
    print("Area of circle:", calculate_area(r))

    print("Division result:", divide_numbers(10, 0))

    p = Person("Bob", 30)
    p.say_hi()

    print("Sum is:", add_numbers(10, 5))
