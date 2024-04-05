#-------------------------------------------------------------------------
# Name:         Hours
# Purpose:		Program that lets you enter a number of hours, and converts it to days AND hours.
# Author:       Teng. M
# Created:      24/3/2024
#-------------------------------------------------------------------------

#output title
print("\n","**hour converter**")

#get number of hours
hours = int(input("Enter number of hours: "))

#converting hours to days and hours
number_of_days = (hours//24)
leftover_hours = (hours%24)

#output
print("\n", hours,"Hours =", number_of_days, "days and" ,leftover_hours,"hours.", "\n")

## new print statement using string concatentation here
print("\n", str(hours) + " Hours = " + str(number_of_days) + " days and " + str(leftover_hours) + " hours.", "\n")

## new print statement using f-strings here.
print("\n", f"{hours} Hours = {number_of_days} days and {leftover_hours} hours.", "\n")