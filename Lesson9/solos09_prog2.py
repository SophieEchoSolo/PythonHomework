import math

"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 09 - Program 2
Description:  solos09_prog2.py - This program will take user input and calculate various statistics with that data
"""

# declare variables and lists to be used
rainfall = []
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# Get user input for the rainfall list
i = 0
while i < len(months):
    rain_amt = input("Enter rain amount in inches for the month of " + months[i] + ": ")
    rainfall.append(float(rain_amt))
    i += 1

#Function to compute the total rainfall for the year
def total_rainfall(rainfall):
    i = 0
    total = 0
    while i < len(rainfall):
        total = total + rainfall[i]
        i += 1
    print("Total rainfall for the year was " + str(round(total,2)))

#Function to compute the average rainfall for the year
def avg_rainfall(rainfall):
    i = 0
    total = 0
    #loop to sum the list
    while i < len(rainfall):
        total = total + rainfall[i]
        i += 1
    avg = round(total / len(rainfall), 1)
    print("Average rainfall for the year was " + str(avg))

#Function to determing the max rainfall for the year
def max_rainfall(rainfall):
    i = 0
    max = -math.inf
    max_month = []
    #Loop to compare the values to determine the max value
    while i < len(rainfall):
        if max < rainfall[i]:
            max = rainfall[i]
            max_month = [months[i]]
        #Find any months with the sam value as the maximum
        elif max == rainfall[i]:
            max_month.append(months[i])
        i += 1
    #prints the result
    print("The month(s) with the highest rainfall was/were " +
          " and ".join(max_month) + " with " + str(max) + " inches")

#Function to determing the min rainfall for the year
def min_rainfall(rainfall):
    i = 0
    min = math.inf
    min_month = []
    #Loop to compare the values to determine the min value
    while i < len(rainfall):
        if min > rainfall[i]:
            min = rainfall[i]
            min_month = [months[i]]
        #Find any months with the sam value as the maximum
        elif min == rainfall[i]:
            min_month.append(months[i])
        i += 1
    #prints the result
    print("The month(s) with the lowest rainfall was/were " +
          " and ".join(min_month) + " with " + str(min) + " inches")

#Main that calls all of the above functions
if __name__ == "__main__":
    total_rainfall(rainfall)
    min_rainfall(rainfall)
    max_rainfall(rainfall)
    avg_rainfall(rainfall)
    print(rainfall)
