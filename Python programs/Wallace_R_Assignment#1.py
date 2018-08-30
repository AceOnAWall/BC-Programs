#-----------------------------------------------------------------------
# Program name: Calculating total sale
# Author: Ryan Wallace
# Date: 2-3-16
# Purpose: To calculate total sale with sales tax
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
# float: saleAmount

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

saleAmount = float(input("Enter the sale amount: "))

print("\nThe sale amount is $" + format(saleAmount, ',.2f'))
print("The sales tax is $" + format(saleAmount * .08, ',.2f'))
print("The total sale is $" + format(saleAmount * .08 + saleAmount, ',.2f'))

input("\nRun complete. Press the Enter key to exit.")

