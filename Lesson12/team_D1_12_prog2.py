def grade_test(student_response_list, answer_list):
    """
    Compares student answers to the answer key and determines grade %
    """
    # creates variable to use for grading
    k = 0
    correct_ans = 0

    # while loop to compare student answers to correct answers
    while k < len(answer_list):
        if student_response_list[k] == answer_list[k]:
            correct_ans += 1
        k += 1

    percent_correct = (correct_ans / (len(answer_list)) * 100)
    print(f"You for {percent_correct}% right on the test")


if __name__ == "__main__":
    print("First, Professor, you need to tell me the answers to your test.")
    # Get user input for number of questions
    q_number = int(input("How many questions will be on the test? "))
    # Create empty answer list
    answer_list = []

    # While loop to ask for answers to the test and to validate the inputs are correct
    i = 0
    while i != q_number:
        ans = input("What is the answer to question #" +
                    str(i+1) + "(A, B, C, D, or E)?: ")
        # Uses .upper to ensure code can handle both upper and lower case
        if ans.upper() in ["A", "B", "C", "D", "E"]:
            answer_list.append(ans.upper())
        else:
            print("Please enter an answer from A, B, C, D, E")
            ans = input("What is the answer to question #" +
                        str(i+1) + "(A, B, C, D, or E)?: ")
        i += 1
    print("The test has been created!")

    # Get student answers
    print("Welcome student. Time to take your test!")
    # Create variables for student
    j = 0
    student_response_list = []

    # While loop to ask for answers from the student and to validate the inputs are correct
    while j < len(answer_list):
        student_ans = input("What is the answer to question #" +
                            str(j+1) + "(A, B, C, D, or E)?: ")
        # Uses .upper to ensure code can handle both upper and lower case
        if student_ans.upper() in ["A", "B", "C", "D", "E"]:
            student_response_list.append(student_ans.upper())
        else:
            print("Please enter an answer from A, B, C, D, E")
            student_ans = input("What is the answer to question #" +
                                str(j+1) + "(A, B, C, D, or E)?: ")
        j += 1

    grade_test(student_response_list, answer_list)
