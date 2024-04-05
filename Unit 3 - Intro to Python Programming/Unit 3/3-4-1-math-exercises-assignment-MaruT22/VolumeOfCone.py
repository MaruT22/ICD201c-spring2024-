#-------------------------------------------------------------------------
# Name:         Volume of a Cone
# Purpose:		program that computes the volume of a sphere given the radius and height from the user.
# Author:       Teng M
# Created:      24/3/2024
#-------------------------------------------------------------------------
import math
#title
print ("\n","**volume of a cone Calculator**")

#getting height and radius of cone
height_cm = float(input("Enter the height (cm): "))
radius_cm = float(input("Enter the radius (cm): "))

#calculating the volume of the cone 
volume_cm = round(((math.pi*(radius_cm**2))*height_cm/3),1)

#output
print("\n", "The volume of your cone is", volume_cm ,"cm^3.")

## new print statement using string concatentation here
print("\n", "The volume of your cone is " + str(volume_cm) + "cm^3.")

## new print statement using f-strings here.
print("\n", f"The volume of your cone is {volume_cm}cm^3.")