#-----------------------------------------------------------------------
# Program name: File Encryption
# Author: Ryan Wallace
# Date: 4*8*16
# Purpose: To encrypt and decrypt files
#-----------------------------------------------------------------------

# FUNCTION DEFINITIONS

def main():
    
    menuSelection = displayMenuAndGetOption()
    
    while menuSelection != "Q":
        if menuSelection == "E":
            abort, fileToCode = getFiles(menuSelection)
            
            if abort == True:
                menuSelection = displayMenuAndGetOption()
                
            codedFile = convert(menuSelection, fileToCode)
            codedFile = input("Enter the output file name: ")
            menuSelection = displayMenuAndGetOption()

        elif menuSelection == "D":
            abort, fileToDecode = getFiles(menuSelection)
            
            if abort == True:
                menuSelection = displayMenuAndGetOption()
                
            decodedFile = convert(menuSelection, fileToCode)
            decodedFile = input("Enter the output file name: ")
            menuSelection = displayMenuAndGetOption()

        else:
            print("Error - Invalid option. Please select again.")
            menuSelection = displayMenuAndGetOption()

    if menuSelection == "Q":
        input("\nRun complete. Press the Enter key to exit.")
        
        
def displayMenuAndGetOption():
    
    print("File Encryption Program\n")
    print("E = Encrypt a file")
    print("D = Decrypt a file")
    print("Q = Quit the program\n")

    userSelection = input("Enter menu selection (E, D, or Q): \n").upper()
    return userSelection


def getFiles(menuSelection):

    if menuSelection == "E":
        abort = False
        toEncryptFile = []
        userInput = input("Enter the file to ENCRYPT. Press Enter alone to abort: ")
        if userInput == "":
            abort = True

        while abort == False:
            try:
                theFile = open(userInput , "r")

                eof = False
                while not eof:
                    toEncryptFile = theFile.readline().strip()
                if toEncryptFile == "":
                    eof = True
                theFile.close()
            
            except IOError:
                print("Error - that file does not exist. Try again.\n")
                abort = True
            
        return abort, toEncryptFile
        

    if menuSelection == "D":
        abort = False
        toDecryptFile = []
        userInput = input("Enter the file to DECRYPT. Press Enter alone to abort: ")
        if userInput == "":
            abort = True

        while abort == False:
            try:
                theFile = open(userInput , "r")

                eof = False
                while not eof:
                    toDecryptFile = theFile.readline().strip()
                if toDecryptFile == "":
                    eof = True
                theFile.close()

            except IOError:
                print("Error - that file does not exist. Try again.")
                abort = True

        return abort, toDecryptFile

        
def convert(option, file):
    
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
    
    if option == "E":
        for item in file:
            #outputFile = file.replace(item, CODE{})
            return outputFile

    elif option == "D":
        for item in file:
            #outputFile = file.replace(item, CODE{}, -1)
            return outputFile

        

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC

main()

