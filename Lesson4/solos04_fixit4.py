"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 04 - Fixits
Description:  solos04_fixit4.py - This program asks the user to select one of 3 different sandwich choices.  It includes a validation loop to ensure that the customer
    does pick one of the valid choices, and reasks if neeeded.
    It is suppossed to print out a message with the sandwich choice.
    The program does run, but the output is incorrect for some of the possible/valid user inputs.
"""


def choose_sandwich():

    # prompts user for unput and provides them with options
    print("For your sandwich choice you may have:  hamburger, cheeseburger, or chicken")
    sandwich_choice = input("What sandwich would you like? ")

    # checks if the user choice is allowed and prompts again if the answer is not allowed
    while(sandwich_choice != "hamburger" and sandwich_choice != "cheeseburger" and sandwich_choice != "chicken"):
        print("You may only choose one of these 3 choices for your sandwich:  hamburger, cheeseburger, or chicken")
        sandwich_choice = input("What sandwich would you like? ")

    # returns varible for later user
    return sandwich_choice


def main():
    """ Get and Display Customer Sandwich choice """

    # calls the choose_sandwich function
    sandwich = choose_sandwich()
    print(f"Your sandwich choice is {sandwich}")


# Invoke main
main()
