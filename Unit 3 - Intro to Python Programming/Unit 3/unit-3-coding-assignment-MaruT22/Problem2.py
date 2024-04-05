#-------------------------------------------------------------------------
# Name:         Bill Calculator
# Purpose:		This program will ask the bank teller for an amount of money greater a 100$ it must be a multiple of 5). The program will then calculate the quanity of bills required to make change. 
# Author:       Teng. M
# Created:      28/3/2024
#-------------------------------------------------------------------------



#output title
print("\n", "** Bill Calculator **")

#User inputs 
entered_amount = int(input("Enter the amount in dollars (must be multiple of 5): "))

#Calculating the quantity of bills required to make change
amount_of_20s = entered_amount // 20
remaining = entered_amount % 20

amount_of_10s = remaining // 10
remaining = remaining % 10

amount_of_5s = remaining // 5

#Answer output
print("\n", "The customer receives:")
print(str(amount_of_20s) + " x $20 bill(s)")
print(str(amount_of_10s) + " x $10 bill(s)")
print(str(amount_of_5s) + " x $5 bill(s)", "\n")

