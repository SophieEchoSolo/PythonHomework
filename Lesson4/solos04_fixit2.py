# import the random module
import random

"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 04 - Fixits
Description:  solos04_fixit2.py - This program is intended to ask the user how many sides there are on their dice.  Then, the program will roll the dice 7 times, and (by calling the roll_dice function)
get the random face value of the dice, and then display the output.
However, this program does not run, it throws a NameError.
"""

# setting up the dice rolling funciton


def roll_dice(number_of_sides):
    """ This function randomly rolls a dice which has a number_of_sides as a parameter, and returns the value.
        For example, if number_of_sides == 6, then the program may return a 1, 2, 3, 4, 5, or 6.
    """
    # Will roll a number based on user input and store it to a variable
    my_roll = random.randint(1, number_of_sides)

    # returns the result of the roll
    return(my_roll)


def main():
    """ This program rolls a dice 7 times, and displays the dice roll. """

    # Asks and stores dice sides
    sides = input("How many sides are there on the dice? ")
    sides = int(sides)

    for i in range(7):
        # roll the dice
        my_roll = roll_dice(sides)
        # display what was rolled
        print(f"You rolled {my_roll} on a {sides}-sided dice")


# Invoke the main function
main()
