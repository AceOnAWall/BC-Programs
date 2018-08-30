#-----------------------------------------------------------------------
# Program name: Conversion program
# Author: Ryan Wallace
# Date: 2-4-16
# Purpose: To convert to the metric system
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
# conversion, temp, distance, weight

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

print("CONVERSION PROGRAM\n")
print("T = Convert Fahrenheit to Celsius")
print("D = Convert Miles to Kilometers")
print("W = Convert Pounds to Kilograms\n")

conversion = input("Select conversion to perform ('T'emperature, or 'D'istance, or 'W'eight)? ").upper()

if conversion == "T":
    temp = float(input("\nPlease enter the temperature in FAHRENHEIT: "))
    print(str(temp) + " fahrenheit is " + str(format((temp - 32) / 1.8,'.3f')) + " celsius.")
elif conversion == "D":
    distance = float(input("\nPlease enter the distance in MILES: "))
    print(str(distance) + " miles is " + str(format(distance / 0.621371192237, '.3f')) + " kilometers.")
elif conversion == "W":
    weight = float(input("\nPlease enter the weight in POUNDS: "))
    print(str(weight) + " pounds is " + str(format(weight / 2.2,'.3f')) + " kilograms.")
else :
    print("Error - invalid option selected.  You may only enter T, D, or W.")

input("\nRun complete. Press the Enter key to exit.")

