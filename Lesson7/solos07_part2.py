"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 07 - Files Part 2
Description:  solos07_part2.py - This program is suppossed to ask the user to input a title and loop through the file displaying the names with that title
"""


def fileLoop():
    '''
    Asks user for file name input and loops through the file printing each line with the input title
    '''
    # Gets user input
    fileName = input("Please enter file name: ")
    charTitle = input("Please enter name of a title: ")
    # attempts to open the file input
    try:
        filePtr = open(fileName)

    # returns an error if the file is not found
    except FileNotFoundError:
        print("File could not be found. Please enter valid file name.")
        exit(-1)

    # loops through the file printing each line
    count = 0
    for line in filePtr:
        if line.startswith(charTitle):
            count += 1
            print(line)
    # print statement showing results
    print(f"{count} names had the title of {charTitle}")
    filePtr.close()


# calls the function fileloop
if __name__ == "__main__":
    fileLoop()
