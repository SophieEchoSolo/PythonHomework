"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 04 - Fixits
Description:  shortname04_fixit3.py - This program asks the user to enter a number of yards.  Then, using a function, the program converts the yards to inches by multiplying by 36.
    This program appears to run, but does not display any output.
"""


def convert_yards_to_inches(yards):
    """ This function converts the yards to a number of inches by multiplying by 36, and returns the calculated number of inches """
    # converts yards to inches and returns the value for later use
    return 36 * yards


def main():
    # takes user input and passes it through the conver_yards_to_inces function
    yards = input("How many yards long? ")
    yards = float(yards)
    inches = convert_yards_to_inches(yards)

    # prints the result to the terminal
    print(f"{yards} yards is equivalent to {inches} inches")


# Invoke main function
main()
