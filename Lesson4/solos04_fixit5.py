"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 04 - Fixits
Description:  shortname04_fixit5.py - This program asks the user for the day of the week, and intends do the following:
    If the day of week is Sunday, the program should display a message saying that today is Sunday, and indicating "waffles" for breakfast.
    If the day of the week is Saturday, the program should display a message saying that today is Saturday, and indicating "toast with jam" for breakfast.
    If the day of the week is any day other than Saturday or Sunday, the program should display a message with the appropriate day of the week, indicating "granola" for breakfast.
    The program does not run successfully, instead it throws a NameError.
"""


def alarm_clock(day_of_week):
    # defines variables
    alarm_setting = ""
    # checks for days of the week and determines alarm setting
    if (day_of_week == "Saturday" or day_of_week == "Sunday"):
        alarm_setting = "Sleep late"
    else:
        alarm_setting = "get up at usual time"

    # returns alarm_setting for later use
    return alarm_setting


def breakfast_food(day_of_week):
    # defines variables
    breakfast = ""
    # checks for days of the week and determines breakfast
    if day_of_week == "Sunday":
        breakfast = "waffles"
    elif day_of_week == "Saturday":
        breakfast = "toast with jam"
    else:
        breakfast = "granola"
    # returns breakfast for later use
    return breakfast


def main():
    # asks user for Input
    today = input(
        "What day is today? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday):  ")
    # invokes the two earlier functions and returns their values
    alarm_setting = alarm_clock(today)
    breakfast = breakfast_food(today)

    # prints the result to the terminal
    print(
        f"Today is {today}! You can {alarm_setting} and have {breakfast} for breakfast !")


# Invoke main
main()
