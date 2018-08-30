#-----------------------------------------------------------------------
# Program name: Pay calculator
# Author: Ryan Wallace
# Date: 2-1-16
# Purpose: to calculate a user's pay
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
# float: hoursWorked , hourlyRate

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

hourlyRate = float(input("enter your hourly rate: "))
hoursWorked = float(input("enter your hours worked: "))
print("your pay for this period is: $", hoursWorked * hourlyRate)

input("\nRun complete. Press the Enter key to exit.")

