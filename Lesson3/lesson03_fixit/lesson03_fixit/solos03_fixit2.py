"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 03 - Fixits
Purpose:  solos03-fixit2.py
	This program is intended to say Hello to the user, ask their name, and what Python topic they want to learn about, and then agree and say Great let's learn about whatever topic the user wants to know about.   It does not run.  
	Your fixed code must still include the name and topic information from the user in the print statements. 
"""

# Greeting the user
message = "Hello Python learner!"
print(message)

# Ask user their name and what they would like to learn
name = input("What is your name?")
topic = input(
    f"Okay, {name} what Python topic would you like to learn about today?")

# Respond with a energetic statement about their topic
print(f"Great, let's learn about {topic}")
