import datetime

# This examples gets user inputs and then determines the difference between the two dates entered
year1 = int(input("Enter a year number: "))
month1 = int(input("Enter a month number: "))
date1 = int(input("Enter a day number: "))

year2 = int(input("Enter another year number: "))
month2 = int(input("Enter another month number: "))
date2 = int(input("Enter another day number: "))


date1 = datetime.date(year1, month1, date1)
date2 = datetime.date(year2, month2, date2)
diff = date1 - date2
print(str(diff.days) + " days between the dates you entered.")

# Shows the dates entered in different formats
print(date1.strftime("%d/%m/%Y"))

print(date1.strftime("%b %d, %Y"))

print(date1.strftime("%B %d, %Y"))

print(date1.strftime("%a %B %d, %Y"))

print(date1.strftime("%A %B %d, %Y"))

print(date1.strftime("%A, %B %d, %Y"))
