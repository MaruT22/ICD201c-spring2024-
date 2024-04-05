#-------------------------------------------------------------------------
# Name:         Circumference
# Purpose:		Program that computes the circumference of a circle given a radius from the user.
# Author:       Teng. M
# Created:      24/3/2024
#-------------------------------------------------------------------------

import math

#title
print ("\n","**Circumference Calculator**")

#getting radius in cm
radius_cm = float(input("Enter the radius (cm): "))

#calculating circumference_cm
circumference_cm = (2 * math.pi * radius_cm)
circumference_cm = round(circumference_cm ,2)
 
#output
print("\n","The circumference of your circle is", circumference_cm ,"cm^2.")

## new print statement using string concatentation here
print("\n","The circumference of your circle is", str(circumference_cm) + "cm^2.")

## new print statement using f-strings here.

print("\n",f"The circumference of your circle is {circumference_cm}cm^2.")