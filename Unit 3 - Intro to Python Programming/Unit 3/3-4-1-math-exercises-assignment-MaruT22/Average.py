#-------------------------------------------------------------------------
# Name:         Average
# Purpose:		A program that calculates the average of a student’s marks. rounding to nearest int.
# Author:       Teng. M
# Created:      2/3/2024
#-------------------------------------------------------------------------

#title
print("**Average Calculator**")

#get grade for courses
course_1 = round(float(input("Enter your mark for Course 1 (%): ")))
course_2 = round(float(input("Enter your mark for Course 2 (%): ")))
course_3 = round(float(input("Enter your mark for Course 3 (%): ")))
course_4 = round(float(input("Enter your mark for Course 4 (%): ")))

#calculating
average_mark = int(((course_1 + course_2 + course_3 + course_4)/4)*1)

#output
print("Your average is", average_mark ,"percent")

## new print statement using string concatentation here
print("Your average is", str(average_mark) + "percent")

## new print statement using f-strings here.
print(f"Your average is {average_mark}percent")
