#-----------------------------------------------------------------------
# Program name: Employee tracker program
# Author: Ryan Wallace
# Date: 4-29-16
# Purpose: To keep track of employee information
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

class Employee:
    def __init__(self, employeeName, employeeNum):
        self.employeeName = employeeName
        self.employeeNum = str(employeeNum)

    def setName(self, employeeName):
        self.employeeName = employeeName

    def setNum(self, employeeNum):
        self.employeeNum = employeeNum

    def getName(self):
        return self.employeeName

    def getNum(self):
        return self.employeeNum

    def __str__(self):
        return "Name: " + self.employeeName + "\n" + \
               "ID number: " + self.employeeNum

class ProductionWorker(Employee):
    def __init__(self, employeeName, employeeNum, shiftNumber, hourlyRate):
        Employee.__init__(self, employeeName, employeeNum)
        self.shiftNumber = shiftNumber
        self.hourlyRate = hourlyRate

    def setShiftNum(self, shiftNumber):
        self.shiftNumber = shiftNumber

    def setHourlyRate(self, hourlyRate):
        self.hourlyRate = hourlyRate

    def getShiftNum(self):
        return self.shiftNumber

    def getHourlyRate(self):
        return self.hourlyRate

    def __str__(self):
        return "Name: " + self.employeeName + "\n" + \
               "ID number: " + self.employeeNum + "\n" + \
               "Shift: " + str(self.shiftNumber) + "\n" + \
               "Hourly Pay Rate: $" + str(self.hourlyRate)

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    userName = input("Enter the name: ")
    userNumber = input("Enter the ID number: ")
    userShift = int(input("Enter the shift number: "))
    userPayRate = format(float(input("Enter the hourly pay rate: ")), ".2f")

    shiftWorker = ProductionWorker(userName, userNumber, userShift, userPayRate)

    print("\nProduction worker information")
    print("-" * 29 + "\n")

    print(shiftWorker)
   
    input("\nRun complete. Press the Enter key to exit.")
    
#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()
