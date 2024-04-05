#-------------------------------------------------------------------------
# Name:         Area of Rectangle
# Purpose:      Finding the area of a rectangle.
# Author:       Teng. M
# Created:      22/3/2024
#-------------------------------------------------------------------------
#title
print ("\n","**Area of a Rectangle Calculator**")

#getting width and length of rectangle
length_cm = float(input("Enter the length (cm): "))
width_cm = float(input("Enter the width (cm): "))

#calculating area
area = (length_cm * width_cm)
 
#output
print ("\n", "The area of your rectangle is", area,"cm^2", "\n")

## new print statement using string concatentation here
print ("\n", "The area of your rectangle is", str(area) + "cm^2", "\n")

## new print statement using f-strings here.
print ("\n", f"The area of your rectangle is {area}cm^2", "\n")
