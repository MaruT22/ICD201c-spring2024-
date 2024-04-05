#-------------------------------------------------------------------------
# Name:		    Lesson 3.3 User Input & Casting
# Purpose:		Homework Questions
# Author:		Last Name. First Initial
#
# Created:		dd/mm/yyyy
#-------------------------------------------------------------------------

# QUESTION #1:
# Write a line of code that will ask the user for the length and width of a rectangle.
# Make sure to store it in a variable and follow the Python Style Guide.
'''
print(" ")
length = input("What is the length of the rectagle? ")
width = input("What is the length of the rectagle? ")
print(" ")

# QUESTION #2:
# Write a program takes the user's first name, last name, and age.
# The program will then output their information

print(" ")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
user_age = input("What is your age? ")
print(" ")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", user_age)
print(" ")

#The output should look like this:
What is your first name? Jane
What is your last name? Doe
What is your age? 23

First Name: Jane
Last Name: Doe
Age: 23
'''

# QUESTION #3:
# Write a program that asks the user for each data type (int, float, string).
# Make sure to store it in a variable and follow the Python Style Guide

string = input("Give me a number")
interger = int(input("Give me a full number "))
flooat = float(input("Give me any number"))
print("string",string)
print("interger",interger)
print("float",flooat)
# Part (a) Convert each type to an int then output the type of each one
int_string = int(string)
int_interger = int(interger)
int_float = int(flooat)
print(type(int_string))
print(type(int_interger))
print(type(int_float))
# Part (b) Convert each type to a float then output the type of each one
float_string = float(string)
float_interger = float(interger)
float_float = float(flooat)
print(type(float_string))
print(type(float_interger))
print(type(float_float))

# Part (c) Convert each type to a string then output the type of each one
str_string = str(string)
str_interger = str(interger)
str_float = str(float)
print(type(float_string))
print(type(float_interger))
print(type(float_float))

# QUESTION #4:
'''
Consider the code below:
# Initialize variables
km_travelled = 300
litres_used = 40

# Calculate the km_per_litres
fuel = km_travelled/litres_used

# Output result
print ("The kilometres per litre for the vehicle is", fuel ,"km/L")
'''

# Part (a) Modify the code to get km_travlled and litres_used values from the user
'''
km_travelled = int(input("How many km have you traveled? "))
litres_used = int(input("How many litres were used? "))
fuel = (km_travelled/litres_used)

print(" ")
print ("The kilometres per litre for the vehicle is", fuel ,"km/L")
print(" ")
# Part (b) Modify the code from part (a) so that it asks the user for the make of the car
# and incorporate this into the final print statement

print(" ")
user_car = input("What type of car do you drive? ")
km_travelled = int(input("How many km have you traveled? "))
litres_used = int(input("How many litres were used? "))
fuel = (km_travelled/litres_used)

print (" ")
print ("You drive a", user_car)
print ("The kilometres per litre for your",user_car,"is", fuel ,"km/L")
'''