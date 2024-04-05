#-------------------------------------------------------------------------
# Name:         Minutes
# Purpose:		program that lets you enter a number of minutes, and converts it to days, hours, AND minutes.
# Author:       Teng M
# Created:      24/3/2024
#-------------------------------------------------------------------------

#output title
print("\n","**minute converter**")

#get number of hours
minutes =int(input("Enter number of minutes: "))

#converting minutes to days and hours and minutes
days = int(round((minutes/60)//24))
leftover_hours = int(round((minutes/60)%24))
leftover_minutes = int(round(minutes%60))

#output
print("\n",minutes ,"minutes =",days,"days", leftover_hours ,"hours and", leftover_minutes ,"minutes.","\n")

## new print statement using string concatentation here
print("\n", str(minutes) + " minutes = " + str(days) + " days " + str(leftover_hours) + " hours and " + str(leftover_minutes) + " minutes." ,"\n")

## new print statement using f-strings here.
print("\n", f"{minutes} minutes = {days} days {leftover_hours} hours and {leftover_minutes} minutes." ,"\n")