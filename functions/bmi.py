def main():
    """Get user input for bmi"""
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = calculate_bmi(height, weight)
    print(f"Your BMI is {bmi}.")


def calculate_bmi(height, weight):
    """Calculates the BMI given a height and weight"""
    # This function has two parameters height and weight
    # It does not ask the user for inputs
    # function returns the result so main function can use it
    return weight / (height ** 2)


main()
