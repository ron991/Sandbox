import math


def get_valid_age(low, high):
    """get valid age from user"""
    # function is to get valid age
    # customised by passing in low and high parameters
    # it does not print, it returns
    age = int(input("Enter your age:"))
    while age < low or age > high:
        print("invalid age")
        age = int(input("Enter your age:"))
    return age


def print_grid(rows, columns):
    """print grid"""
    # function is to print grid of *'s
    # customised by passing in rows and columns parameters
    # does not get user input, it takes arguments
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()


print_grid(3, 7)


def calculate_circle_area(radius):
    """calculate circle area"""
    return math.pi * radius ** 2


# Void function to test for calculate_circle_area
print(calculate_circle_area(5))
