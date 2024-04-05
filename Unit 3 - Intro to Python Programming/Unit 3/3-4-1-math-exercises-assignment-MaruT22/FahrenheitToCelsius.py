#-------------------------------------------------------------------------
# Name:         Fahrenheit to Celsius
# Purpose:		Translates the tempurature in Fahrenheit to Celsius
# Author:       Teng. M
# Created:      22/3/2024
#-------------------------------------------------------------------------


#output title
print("\n","**Fahrenheit to Celsius Converter**")

#get tempurature from user in fahrenheit 
temp_fahrenheit =int(input("Enter tempurature in Fahrenheit: "))

#celsius = 5/9(F - 32)
#convert tempurature fahrenhiet to temp celsius
temp_celsius = (5/9) * (temp_fahrenheit-32)
temp_celsius = round(temp_celsius)
temp_celsius = int(temp_celsius)

#output the temp in celsius

print ("\n", temp_fahrenheit ,"degrees fahrenheit is", temp_celsius ,"degrees celsius.", "\n")

## new print statement using string concatentation here
print ("\n", str(temp_fahrenheit) + " degrees fahrenheit is " + str(temp_celsius) + " degrees celsius.", "\n")

## new print statement using f-strings here.
print ("\n", f"{temp_fahrenheit} degrees fahrenheit is {temp_celsius} degrees celsius.", "\n")