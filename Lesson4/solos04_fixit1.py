"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 04 - Fixits
Description:  solos04_fixit1.py - This program is suppossed to ask the user to input a score, and display the grade (A, B, C, D, or F) for that score using the standard.
    The program does run, but it displays a grade of "None" regardless of the score the user enters.  So, it needs to be fixed !
The Problem: explain the cause of the problem in your own words
The Solution:  fix the code so it runs, and explain how you solved the  problem here
"""


def compute_grade(score):
    """ This function computes a grade of A, B, C, D, F based on score, and returns the letter grade. """
    # define score ranges
    a_score = 90
    b_score = 80
    c_score = 70
    d_score = 60

    # initialize variable named letter_grade
    letter_grade = ''

    # determine the letter grade for the score provided
    if score >= a_score:
        letter_grade = 'A'
    elif score >= b_score:
        letter_grade = 'B'
    elif score >= c_score:
        letter_grade = 'C'
    elif score >= d_score:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    # return the result for later use
    return letter_grade


def main():
    """ This program computes and displays a letter grade for a score """
    # ask student for input and assign it to a variable
    student_score = input("What is your score? ")
    student_score = float(student_score)

    # call the grade function and output the result
    grade = compute_grade(student_score)
    print(f"You receive a(n) {grade} for your score of {student_score}")


# invoke main
main()
