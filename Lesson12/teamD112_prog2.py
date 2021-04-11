"""
Author:  Sophie Solo and Kyle Howell
Course:  CSC 121
Assignment:  Lesson 12 - Program 2
Description:  teamD112_prog2.py - This program will generate a test and answer key, administer the test, and grade the test
"""

def grade_test(student_response_list, answer_list):
    """ 
    Function used to grade the test taken by the student. Will take the number of correct answers, then divide it by the length of the answer list times 100 to determine a percentage.
    """
    # creates variable to use for grading
    k = 0
    correct_ans = 0  # variable that increments for every correct answer given

    # while loop to compare student answers to correct answers
    # loop occurs as long as the number of given answers is less than the length of the answer list
    while k < len(answer_list):
        # if the student's answer is the same as the answer of the corresponding question on the answer list, one is added to the correct_ans variable
        if student_response_list[k] == answer_list[k]:
            correct_ans += 1
        # will increment regardless of whether a student's answer is correct or not until the number of answers given is the same as the length of the answer list.
        k += 1

    percent_correct = ((correct_ans)/(len(answer_list))*100)
    print(f"You got {percent_correct}% right on the Test")


# main function that first generates a test using one user's inputs (The "Professor"), then has a second user (the "Student") take the test.
if __name__ == "__main__":  # main function
    print("Welcome to the Multiple Choice Test Generator!")
    print("First, Professor, you need to tell me the answers to your test.")
    # Get user input for number of questions
    q_number = int(
        input("How many questions do you want to ask on the test you are creating? "))
    # Create empty answer list
    answer_list = []

    # While loop to ask for answers to the test and to validate the inputs are correct
    i = 0
    while i != q_number:
        ans = input("What is the answer to question " +
                    str(i+1) + "(A, B, C, D, or E)?: ")
        # Uses .upper to ensure code can handle both upper and lower case
        # appends the answer to the answer list if any valid answer is entered
        if ans.upper() in ["A", "B", "C", "D", "E"]:
            answer_list.append(ans.upper())
            i += 1
        # will execute if the user entered anything other than a valid answer, displaying an error message then asking the question again
        while ans.upper() != "A" and ans.upper() != "B" and ans.upper() != "C" and ans.upper() != "D" and ans.upper() != "E":
            print(
                "Sorry, but that is not a valid answer. You must enter A, B, C, D, or E.")
            ans = input("What is the answer to question " +
                        str(i+1) + "(A, B, C, D, or E)?: ")

            # appends the answer to the answer list if any valid answer is entered
            if ans.upper() in ["A", "B", "C", "D", "E"]:
                answer_list.append(ans.upper())
                i += 1

    print("Okay, the Test is now Ready for Students to take the Test.")

    # Get student answers
    print("Welcome student! Good Luck on Your test!")
    # Create variables for student
    j = 0
    student_response_list = []

    # While loop to ask for answers from the student and to validate the inputs are correct
    while j < len(answer_list):
        student_ans = input("What is the answer to question " +
                            str(j+1) + "(A, B, C, D, or E)?: ")
        # Uses .upper to ensure code can handle both upper and lower case
        if student_ans.upper() in ["A", "B", "C", "D", "E"]:
            student_response_list.append(student_ans.upper())
            j += 1
        while student_ans.upper() != "A" and student_ans.upper() != "B" and student_ans.upper() != "C" and student_ans.upper() != "D" and student_ans.upper() != "E":
            print(
                "Sorry, but that is not a valid answer. You must enter A, B, C, D, or E.")
            student_ans = input("What is the answer to question " +
                                str(j+1) + "(A, B, C, D, or E)?: ")
            if student_ans.upper() in ["A", "B", "C", "D", "E"]:
                student_response_list.append(student_ans.upper())
                j += 1

    # invokes the grade_test function at the end of the program
    grade_test(student_response_list, answer_list)
