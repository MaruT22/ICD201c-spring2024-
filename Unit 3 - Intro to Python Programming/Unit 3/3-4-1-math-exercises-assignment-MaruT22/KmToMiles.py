#-------------------------------------------------------------------------
# Name:         Km to Miles
# Purpose:		Program that lets the user enter a distance in kilometers and converts it into miles. 
# Author:       Teng. M
# Created:      24/3/2024
#-------------------------------------------------------------------------

#output title
print("\n","**Km to Miles Converter**")

#get distance in km
distance_in_km =float(input("Enter the distance in km: "))

#converting km to miles
distance_in_miles=round((distance_in_km*0.621371),2)

#output
print("\n",distance_in_km,"km is",distance_in_miles,"mi.","\n",)

## new print statement using string concatentation here
print("\n",str(distance_in_km) + " km is " + str(distance_in_miles) + "mi.","\n",)

## new print statement using f-strings here.
print("\n", f"{distance_in_km}km is {distance_in_miles}mi." ,"\n",)