"""

Author:  Sophie Solo

Course:  CSC 121

Assignment:  Lab: Lesson 02 - Variables - Individual

Description:  Converts user input from celsius to fahrenheit

"""

# Input - Ask user for tempterature input in celsius
celsius = input("Enter temperature in Celsius: ")

# Convert the user input from string to float
celsius = float(celsius)

# Processing - Convert from Celsius to Fahrenheit

fahrenheit = celsius * 9/5 + 32.0

# Output - display the result for the user
print("The temperature in Fahrenheit is: ", fahrenheit)
