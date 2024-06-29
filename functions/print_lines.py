"""
Test out functions
"""


def full_names(first_name, last_name):
    """Get full names of names given as argument"""
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name, last_name


full_names("Ron", "Kelly")


def print_line():
    """Print line"""
    # Simple void function
    print('-' * 5)


print_line()


def print_lines(length):
    """Print lines """
    # Parameter to customise the function
    print('-' * length)


print_lines(5)


# def main():
#     print_lines(20)
#     print("Welcome")
#     print_lines(8)
#
#
# main()

# def print_grids(number_of_rows, number_of_columns):
#     # version 1
#     for i in range(number_of_rows):
#         for j in range(number_of_columns):
#             print('*', end="")
#         print()

# print_grids(3, 7)

# def print_grids(number_of_rows, number_of_columns):
#     # version 2
#     for i in range(number_of_rows):
#         print('*' * number_of_columns)
#
#
# print_grids(3, 7)

# def print_grids(number_of_rows, number_of_columns):
#     # version 3
#     print(f"{'*' * number_of_columns}\n" * number_of_rows)
#
#
# print_grids(3, 7)
