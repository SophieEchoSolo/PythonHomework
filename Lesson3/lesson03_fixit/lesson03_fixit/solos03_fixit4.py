"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 03 - Fixits
Purpose:  solos03-fixit4.py  
	This program intends to ask the user for the day of the week.  If the user says it is either Saturday or Sunday, then the program is to
	display that the user can sleep late and have a pancake breakfast, otherwise the program is to display that the user has to get up early and can have a granola
	bar breakfast.
	The program does run, but the output is incorrect for some of the possible/valid user inputs.
"""

# Receive user input for day of the week
today = input(
    "What day is today? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday):  ")

# Check for a weekend day
if (today == "Sunday" or today == "Saturday"):
    print("I can sleep in late")
    print("I can have pancakes for breakfast")
# if the day is a weekday then respond with the following statements
else:
    print("I have to get up early")
    print("I only have time to grab a granola bar for breakfast")
