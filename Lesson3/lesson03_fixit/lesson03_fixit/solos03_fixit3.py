"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 03 - Fixits
Purpose:  solos03-fixit3.py  - This program intends to ask the user for the current year and then ask the user how many years they want to wait. 
	The program then computes the year when their wait will be finished, and displays meaningful/labeled output. 
	The program does run, but the output is incorrect.  
"""

# Receive user inputs for years to wait and the current year
current_year_input = input("what is the current year? ")
wait_years_input = input("How many years do you want to wait? ")

# Convert inputs from strings to integers
current_year = int(current_year_input)
wait_years = int(wait_years_input)

# Calculate the result of adding the variables together
done_year = current_year + wait_years

# Tell the user what year their wait will be over
print(
    f"If you wait {wait_years} years from now, it will be the year {done_year}")
