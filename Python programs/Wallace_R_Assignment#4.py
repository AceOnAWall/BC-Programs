#-----------------------------------------------------------------------
# Program name: Conversion program
# Author: Ryan Wallace
# Date: 3-6-16
# Purpose: To convert to the metric system
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
#

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions
def main():
    getMenuSelection()
    getValueToConvert(getMenuSelection)
    calculateKilometers(getValueToConvert)
    printResult(finalResults)

def getMenuSelection():
    print("CONVERSION PROGRAM\n")
    print("T = Convert Fahrenheit to Celsius")
    print("D = Convert Miles to Kilometers")
    print("W = Convert Pounds to Kilograms\n")

    value = input("Select conversion to perform ('T'emperature, or 'D'istance, or 'W'eight, or 'Q'uit)? ").upper()
    return value

def getValueToConvert(getMenuSelection):
    value = input("Select conversion to perform ('T'emperature, or 'D'istance, or 'W'eight, or 'Q'uit)? ").upper()
    while value != "Q":
        if value == "T":
            tempFahrenheit = float(input("\nPlease enter the temperature in FAHRENHEIT: "))
            return tempFahrenheit
        elif value == "D":
            miles = float(input("\nPlease enter the distance in MILES: "))
            return miles
        elif value == "W":
            pounds = float(input("\nPlease enter the distance in MILES: "))
            return pounds
    if value == "Q":
        input("\nRun complete. Press the Enter key to exit.")
    else :
        print("Error - invalid option selected.  You may only enter T, D, W, or Q.")

def calculateKilometers(getValueToConvert):
    finalKilometers = (miles / 0.6214,'.3f')
    return finalKilometers

def calculateKilograms(getValueToConvert):
    finalKilograms = (pounds / 2.2,'.3f')
    return finalKilograms

def calculateCelsius(getValueToConvert):
    finalCelsius = ((tempFahrenheit - 32) / 1.8,'.3f')
    return finalCelcius

def printResult(finalResults):
    value = getValueToConvert(getMenuSelection) 
    if value == "T":
        print(tempFahrenheit, "degrees Fahrenheit is", finalCelsius, "degrees Celsius.")
    if value == "D":
        print(miles, "miles is", finalKilometers, "kilometers.")
    if value == "W":
        print(pounds, "pounds is", finalKilograms, "kilograms.")

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

main()

input("\nRun complete. Press the Enter key to exit.")

