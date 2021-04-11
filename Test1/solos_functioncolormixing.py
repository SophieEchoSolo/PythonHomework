def color_mixing(color1, color2):
    # Checks for colors being the same
    if color1 == color2:
        print(color1)
    # First checks for red in either 1st or 2nd slot
    if color1 == "red" or color2 == "red":
        # Then checks for blue or yellow in the matching slot
        if color1 == "blue" or color2 == "blue":
            print("purple")
        if color1 == "yellow" or color2 == "yellow":
            print("orange")
    # First checks for blue in either 1st or 2nd slot
    if color1 == "blue" or color2 == "blue":
        # Since red+blue matching was covered above we only need to check for yellow here
        if color1 == "yellow" or color2 == "yellow":
            print("green")


# Main statement asking for user input
if __name__ == "__main__":
    color1 = input("Enter color 1: ")
    color2 = input("Enter color 2: ")
    color_mixing(color1, color2)
