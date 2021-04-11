"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 03 - Fixits
Purpose:  solos03-fixit1.py 
	This program is suppossed to ask the user to input a score, and display the grade (A, B, C, D, or F) for that score using the standard.  The program does not run, and needs to be fixed.
"""

# Setting grading criteria
a_score = 90
b_score = 80
c_score = 70
d_score = 60

# Get user input of the score
score = input('What is the score?')
# Convert input string into float value so that it can be evaluated properly
score = float(score)

# Compare the input score with the grading criteria and print the result
if score >= a_score:
    print('The  grade is A.')
elif score >= b_score:
    print('The grade is B.')
elif score >= c_score:
    print('Your grade is C.')
elif score >= d_score:
    print('The grade is D')
else:
    print('The grade is F')
