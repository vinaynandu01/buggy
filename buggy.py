# buggy_script_no_syntax_errors.py

def greet_user(name):
    if name == "":
        print("Hello, Stranger!")  # Should be handled better
    else:
        print("Hello, " + name)

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

def divide_numbers(a, b):
    return a / b  # May cause ZeroDivisionError

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi, my name is", self.name)

def add_numbers(x, y):
    result = x - y  # Logical error: should be x + y
    return result

if __name__ == "__main__":
    greet_user("")  # Should probably ask for name if empty

    r = "5"  # Logical bug: should be a number, not a string
    print("Area of circle:", calculate_area(r))  # Will throw TypeError

    print("Division result:", divide_numbers(10, 0))  # Runtime error

    p = Person("Bob", 30)
    p.say_hi()

    print("Sum is:", add_numbers(10, 5))  # Will return 5 instead of 15
