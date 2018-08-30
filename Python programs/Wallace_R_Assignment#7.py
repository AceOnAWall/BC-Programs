#-----------------------------------------------------------------------
# Program name: Car radio simulator 
# Author: Ryan Wallace
# Date: 4-22-16
# Purpose: To create a program that simulates a car radio
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS (Use only until functions)
#
# Variable Type: Variable list separated by commas

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

class Radio:
    
    STATIONS = {0:"STATIC", 1:"97.2", 2:"99.6", 3:"101.7", 4:"105.3", 5:"108.5"}

    def __init__(self):
        self.preset1 = 0
        self.preset2 = 0
        self.preset3 = 0
        self.currentlyTuned = 0

    def seekNext(self):
        self.currentlyTuned += 1

    def longPressPreset1(self, key):
        self.preset1 = key

    def longPressPreset2(self, key):
        self.preset2 = key

    def longPressPreset3(self, key):
        self.preset3 = key

    def shortPressPreset1(self, key):
        self.currentlyTuned = key

    def shortPressPreset2(self, key):
        self.currentlyTuned = key

    def shortPressPreset3(self, key):
        self.currentlyTuned = key

    def displayLCD(self):
        try:
            print("Currently tuned:", Radio.STATIONS[self.currentlyTuned])

        except KeyError:
            self.currentlyTuned = 1
            print("Currently tuned:", Radio.STATIONS[self.currentlyTuned])
            
    def __str__(self):
        return "Preset 1: " + Radio.STATIONS[self.preset1] + "\nPreset 2: " \
               + Radio.STATIONS[self.preset2] + "\nPreset 3: " + Radio.STATIONS[self.preset3]
        

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    
    myRadio = Radio()
    myRadio.displayLCD()
    option = displayMenuGetOption()

    while option != "10":
        
        if option == "1":
            myRadio.displayLCD()
            
        elif option == "2":
            myRadio.longPressPreset1(myRadio.currentlyTuned)
            
        elif option == "3":
            myRadio.longPressPreset2(myRadio.currentlyTuned)
            
        elif option == "4":
            myRadio.longPressPreset3(myRadio.currentlyTuned)
            
        elif option == "5":
            myRadio.seekNext()
            
        elif option == "6":
            myRadio.shortPressPreset1(myRadio.currentlyTuned)
            
        elif option == "7":
            myRadio.shortPressPreset2(myRadio.currentlyTuned)
            
        elif option == "8":
            myRadio.shortPressPreset3(myRadio.currentlyTuned)
            
        elif option == "9":
            print(myRadio)
            
        else:
            myRadio.displayLCD()
            option = displayMenuGetOption()
        
        myRadio.displayLCD()   
        option = displayMenuGetOption()
            
    if option == "10":
        input("Run complete. Press the Enter key to exit.")


def displayMenuGetOption():

    print("\n1 = Display tuned in station")
    print("2 = Program preset station 1")
    print("3 = Program preset station 2")
    print("4 = Program preset station 3")
    print("5 = Seek next staion")
    print("6 = Tune preset station 1")
    print("7 = Tune preset station 2")
    print("8 = Tune preset station 3")
    print("9 = Dump programming")
    print("10 = Turn off radio\n")

    selection = input("Enter option: ")
    print("")
    return selection
    
    
#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()

