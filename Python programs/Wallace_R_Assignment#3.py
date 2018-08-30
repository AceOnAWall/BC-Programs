#-----------------------------------------------------------------------
# Program name: Voter eligibility and polling station program
# Author: Ryan Wallace
# Date: 2-29-16
# Purpose: To find locations to vote
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
# int: userAge, zipCode

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

print("VOTER ELIGIBILITY AND POLLING STATION PROGRAM\n\n")

userAge = int(input"Enter your age (Type '0' to exit program): "))

while userAge in range(1,18):
    print("\nYOU ARE INELIGIBL5E TO VOTE.")
    userAge = int(input("\nEnter your age (Type '0' to exit program): ")) 
           
while userAge >= 18:
    zipCode = int(input("\n\tEnter your residence's zip code: "))
    if zipCode == 93305:
        print("\tYour polling station is 123 Panorama Drive.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    elif zipCode == 93306:
        print("\tYour polling station is 6143 Fairfax Drive.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    elif zipCode == 93307:
        print("\tYour polling station is 21121 B Street.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    elif zipCode == 93308:
        print("\tYour polling station is 863 Desmond Ct.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    elif zipCode == 93309:
        print("\tYour polling station is 7332 Del Canto Ct.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    else:
        print("\tError - Unknown zip code.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))
    while userAge <= 17 and userAge >= 1:
        print("\n\tYOU ARE INELIGIBLE TO VOTE.")
        userAge = int(input("\nEnter your age (Type '0' to exit program): "))   
if userAge == 0:
    input("\nRun complete. Press the Enter key to exit.")

