#-----------------------------------------------------------------------
# Program name: ZIP code lookup
# Author: Ryan Wallace
# Date: 3-29-16
# Purpose: To find a city and state for a given zip code
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS

zips = []
cities = []
states = []

def main():
    
    getLists()
    userInput = promptUser()

    while userInput != "":
        if userInput in zips:
            city, state = findZipCode(userInput)
            printResults(city, state)
            userInput = promptUser()

        elif userInput not in zips:
            print("\n\t\tThe zip code does not exist\n")
            userInput = promptUser()
            
    if userInput == "":
        input("\nRun complete. Press the Enter key to exit.")

def getLists():

    try:
        theFile = open("zipcodes.txt" , "r")
    
        for line in theFile:
            extracted = line.split(",")
            zips.append(extracted[0])
            cities.append(extracted[1])
            states.append(extracted[2])
         
        theFile.close()

    except IOError:
        print("Error - zipcodes.txt does not exist.")
        

def promptUser():

    userZipCode = input("Enter a zip code to find (Press Enter key alone to stop): ")
    return userZipCode


def findZipCode(zipCodeToFind):

    if zipCodeToFind in zips:
        indexNumber = zips.index(zipCodeToFind)
        cityToFind = (cities[indexNumber])
        stateToFind = (states[indexNumber])

        return cityToFind, stateToFind
    

def printResults(city, state):

    print("\n\t\tThe city is " + city, "and the state is " + state)
        
    
#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

main()
