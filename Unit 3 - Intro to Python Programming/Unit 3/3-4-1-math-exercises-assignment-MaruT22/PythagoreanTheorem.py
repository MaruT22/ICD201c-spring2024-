#-------------------------------------------------------------------------
# Name:         Pythagorean Theorem
# Purpose:		program that takes the lengths of the two legs (a and b) of a right-angle triangle from the user and apply the Pythagorean Theorem to find the hypotenuse (c).
# Author:       Teng M
# Created:      24/3/2024
#-------------------------------------------------------------------------
import math
#title
print ("\n","**Hypotenuse Calculator**")

#getting  and length of rectangle
length_side_a = float(input("Enter the length of side a: "))
length_side_b = float(input("Enter the length of side b: "))

#calculating Hypotenuse
length_side_c = math.sqrt((length_side_a**2)+(length_side_b**2))
length_side_c = round(length_side_c,1)
#output
print("\n", "The hypotenuse of a right triangle with legs", length_side_a ,"and", length_side_b ,"is", length_side_c ,"units.")

## new print statement using string concatentation here
print("\n", "The hypotenuse of a right triangle with legs " + str(length_side_a) + " and " + str(length_side_b) + " is " + str(length_side_c) + " units.")

## new print statement using f-strings here.
print( "\n", f"The hypotenuse of a right triangle with legs {length_side_a} and {length_side_b} is {length_side_c} units.")