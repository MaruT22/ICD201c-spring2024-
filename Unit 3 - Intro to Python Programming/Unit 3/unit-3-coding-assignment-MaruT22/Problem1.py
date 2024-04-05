#-------------------------------------------------------------------------
# Name:         Midpoint of a Line Calculator
# Purpose:      This is a program where it takes two user input points and calculates the midpoint of the line.
# Author:       Teng. M
# Created:      28/3/2024
#-------------------------------------------------------------------------



#output title
print("\n", "** Midpoint of a Line Calculator **")

#User inputs 
x_cord_1 = float(input("Enter the x coordinate of point 1: "))
y_cord_1 = float(input("Enter the y coordinate of point 1: "))
x_cord_2 = float(input("Enter the x coordinate of point 2: "))
y_cord_2 = float(input("Enter the y coordinate of point 2: "))

#Calculating and rounding the midpoint of point 1 and point2
midpoint_x = (x_cord_1 + x_cord_2) / 2
midpoint_y = (y_cord_1 +y_cord_2) / 2
midpoint_x = round(midpoint_x, 1)
midpoint_y = round(midpoint_y, 1)

#output answer
print("\n", f"The midpoint between ({x_cord_1},{y_cord_1}) and ({x_cord_2},{y_cord_2}) is ({midpoint_x},{midpoint_y})." ,"\n")