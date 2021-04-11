"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 06 - Morse Code
Description:  solos06_morsecode.py - This program is suppossed to ask the user to input a string and it will return the morse code version of that string
"""

# function to compare letters in the string to morse code characters
# this function uses the .upper statement to eliminate the issue with case sensitivity


def convert_letter_to_morse(letter):
    """
    Function to return the morse code version of each letter.
    """
    if letter.upper().startswith('A'):
        letter = '.-'
    elif letter.upper().startswith('B'):
        letter = '-...'
    elif letter.upper().startswith('C'):
        letter = '-.-.'
    elif letter.upper().startswith('D'):
        letter = '-..'
    elif letter.upper().startswith('E'):
        letter = '.'
    elif letter.upper().startswith('F'):
        letter = '..-.'
    elif letter.upper().startswith('G'):
        letter = '--.'
    elif letter.upper().startswith('H'):
        letter = '....'
    elif letter.upper().startswith('I'):
        letter = '..'
    elif letter.upper().startswith('J'):
        letter = '.---'
    elif letter.upper().startswith('K'):
        letter = '-.-'
    elif letter.upper().startswith('L'):
        letter = '.-..'
    elif letter.upper().startswith('M'):
        letter = '--'
    elif letter.upper().startswith('N'):
        letter = '-.'
    elif letter.upper().startswith('O'):
        letter = '---'
    elif letter.upper().startswith('P'):
        letter = '.--.'
    elif letter.upper().startswith('Q'):
        letter = '--.-'
    elif letter.upper().startswith('R'):
        letter = '.-.'
    elif letter.upper().startswith('S'):
        letter = '...'
    elif letter.upper().startswith('T'):
        letter = '-'
    elif letter.upper().startswith('U'):
        letter = '..-'
    elif letter.upper().startswith('V'):
        letter = '...-'
    elif letter.upper().startswith('W'):
        letter = '.--'
    elif letter.upper().startswith('X'):
        letter = '-..-'
    elif letter.upper().startswith('Y'):
        letter = '-.--'
    elif letter.upper().startswith('Z'):
        letter = '--..'
    return letter

# main method that asks for user input and then loops through the string to return the morse code


def main():
    """
    Main method that asks for input and returns the result of the conversion
    """
    # asks for user input
    word = input("Enter a string and I will convert it to morse code: ")
    # initializes empty string
    new_morse = ""
    # loops through the string and calls the conversion statement
    for letter in word:
        result = convert_letter_to_morse(letter)
        new_morse = new_morse + result
    # prints the result
    print(new_morse)


# calls the main method
if __name__ == "__main__":
    main()
