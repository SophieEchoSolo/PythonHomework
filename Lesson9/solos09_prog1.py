import random

"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 09 - Program 1
Description:  solos09_prog1.py - This program will generate random numbers and then sort them into even and odd lists
"""

# create empty lists that will be used throughout the program
rand_list = []
odd_nums = []
even_nums = []

# declare variables
i = 0

# while loop to fill the new_num list with random integers
while i < 20:
    new_num = random.randint(0, 100)
    rand_list.append(new_num)
    i += 1


def is_odd(rand_list):
    """
    Checks if a number is odd or even and adds them to the appropriate list
    """
    # for loop to loop through rand_list
    for num in rand_list:
        # checks for even and odd numbers
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)


# Calls the function and prints the results
if __name__ == "__main__":
    is_odd(rand_list)

    print(rand_list)
    print(even_nums)
    print(odd_nums)
