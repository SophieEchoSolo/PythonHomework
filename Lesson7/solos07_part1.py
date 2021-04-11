"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 07 - Files Part 1
Description:  solos07_part1.py - This program is suppossed to ask the user to input a file name and loop through the file displaying the names
"""


def fileLoop():
    '''
    Asks user for file name input and loops through the file printing each line
    '''
    # Gets user input
    fileName = input("Please enter file name: ")
    # attempts to open the file input
    try:
        filePtr = open(fileName)

    # returns an error if the file is not found
    except FileNotFoundError:
        print("File could not be found. Please enter valid file name.")
        exit(-1)

    # loops through the file printing each line
    for line in filePtr:
        print(line)
    filePtr.close()


# calls the function fileloop
if __name__ == "__main__":
    fileLoop()
