#-----------------------------------------------------------------------
# Program name: 
# Author: 
# Date: 
# Purpose:
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS

#-----------------------------------------------------------------------
# CLASS DEFINITIONS

#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS

def main():
    # Function Variable Definitions
    print("File Encryption Program")
    decision = displayMenuAndGetOption()
    while decision != "Q":
        if decision == "E":
            prompt = "ENCRYPT"
            abort, inputFile, outPutFile, theFile = getFiles(prompt)
            if abort == "Quit":
                decision = "Q"
            convert(inputFile,outPutFile, theFile)  
        elif decision == "D":
            prompt = "DECRYPT"
            abort, inputFile, outPutFile, theFile = getFiles(prompt)
            if abort == "Quit":
                decision = "Q"
            convert(inputFile, outPutFile)
        else:
            print("\nError - Invalid option. Please select again.")
        decision = displayMenuAndGetOption()
    input("\nRun complete. Press the Enter key to exit.")

def displayMenuAndGetOption():
    # Function Variable Definitions
    print("\nE = Encrypt a file")
    print("D = Decrypt a file")
    print("Q = Quit the program")
    userInput = input("\nEnter menu selection (E, D, or Q): ").upper()
    return userInput
    
def getFiles(prompt):
    # Function Variable Definitions
    if prompt == "DECRYPT":
        encryptedFile = input("\nEnter the file to DECRYPT. Press Enter alone to abort: ")
        while encryptedFile != "":
            try:
                fileInput = open(encryptedFile,"r")
            except IOError:
                print("Error that file does not exist. Try again.")
                encryptedFile = input("\nEnter the file to DECRYPT. Press Enter alone to abort: ")  
            outputFileObject, theFile = getOutputFile()
            abort = "continue"
            if outputFileObject == "":
                abort = "Quit"
            return abort, fileInput, outputFileObject, theFile
        else:
            abort = "Quit"
            fileInput = "null"
            outputFileObject = "null"
            return abort, fileInput, outputFileObject
        
    elif prompt == "ENCRYPT":
        unEncryptedFile = input("\nEnter the file to ENCRYPT. Press Enter alone to abort: ")
        while unEncryptedFile  != "":
            try:
                fileInput = open(unEncryptedFile,"r")
            except IOError:
                print("Error that file does not exist. Try again.")
                unEncryptedFile = input("\nEnter the file to ENCRYPT. Press Enter alone to abort: ")
            outputFileObject, theFile = getOutputFile()
            abort = "continue"
            if outputFileObject == "":
                abort = "Quit"
            return abort, fileInput, outputFileObject, theFile
        else:
            abort = "Quit"
            fileInput = "null"
            outputFileObject = "null"
            return abort, fileInput, outputFileObject

def getOutputFile():
    theFile = input("Enter the output file name: ")
    if theFile != "":
        outputFile = open(theFile,"w")
        outputFile.close()
        return outputFile, theFile
    return theFile
def convert(inputFile, outputFile, theFile):
    # Function Variable Definitions

    # Encryption and decryption are inverse of one another
    
    CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}
    
    for lines in inputFile:
        for letters in lines:
            letters = CODE.get(letters, "")
           # print(letters, end =" ")
            outputFile = open(theFile, "a")
            outputFile.write(letters)
            outputFile.close()
#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()

