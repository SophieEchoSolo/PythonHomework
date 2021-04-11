"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 03 - Fixits
Purpose:  solos03-fixit5.py
    This program asks the user for the day of the week, and intends do the following:
    If the day of week is Sunday, the program should display a message saying that today is Sunday, and indicating "waffles" for breakfast.
    If the day of the week is Saturday, the program should display a message saying that today is Saturday, and indicating "toast with jam" for breakfast.
    If the day of the week is any day other than Saturday or Sunday, the program should display a message with the appropriate day of the week, indicating "granola" for breakfast.
    Finally, if the day of the week is Saturday or Sunday, the program should say "I will sleep late", otherwise the program should say "I will set my alarm for the usual time"
    The program does not run successfully, instead it produces an error message
"""

# Asks user for day of the week
today = input(
    "What day is today? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday):  ")

# Checks for sunday and sets the proper responses
if (today == "Sunday"):
    breakfast_food = "waffles"
    alarm = "off"
# Checks for Saturday and sets the proper responses
elif (today == "Saturday"):
    breakfast_food = "toast with jam"
    alarm = "off"
# Checks for any other day and sets the proper responses
else:
    breakfast_food = "granola"
    alarm = "on"

# Prints the statement based on the day and breakfast food
print(f"Today is {today}, and for breakfast I will have {breakfast_food}")

# Sets the reponse in regards to the alarm
if (alarm != "off"):
    print("I will set my alarm for the usual time")
else:
    print("I will sleep late")
