### ORD & CHR HOMEWORK REFACTORED

# imports libraries for use (json to read a json file and stats to find the modal value of a list)
import json
from statistics import StatisticsError, mode


def menu():
    menuSelect = input("1: Encrypt\n2: Decrypt\n3: Exit\n") # asks the user for an option

    if menuSelect == "1": # runs the subroutines to encrypt a message
        mP = message()
        encrypt(mP)

    elif menuSelect == "2": # Runs the subroutines to decrypt a message
        mP = message()
        formedList = decrypt(mP)
        jsonCheck(formedList)
    
    elif menuSelect == "3": # exits the program if the uses selects "3"
        print("Goodbye!")
        exit()
    
    else: # Run the Menu if an option other than 1, 2 or 3 is selected
        menu()
        
# Gets the user's message and splits each word into an element of a list
def message():
    print("#-"*25)
    message = input("Input the message: ")
    messageParts = message.split(" ")
    return messageParts


## Defines a subroutine to Encrypt messages
def encrypt(messageParts):
    # Requests a number of spaces to displace the letters
    key = int(input("What would you like to encrypt by: "))
    
    # Encrypts each letter by the key and returns the result
    for word in messageParts:

        for j in range(len(word)):
            letter = word[j]
            value = ord(letter)
            if not letter.isalpha():
                print(letter, end="")
            else:
                if letter.isupper():

                    if value + key > 90:
                        chrCode = value + key - 90
                        newChr = 64 + chrCode
                    else:
                        newChr = value + key

                elif letter.islower():

                    if value + key > 122:
                        chrCode = value + key - 122
                        newChr = 96 + chrCode
                    else:
                        newChr = value + key

            
                print(chr(newChr), end = "")

        print(end=" ")
    
    print()
    print("#-"*25)
    menu()

## Defines a subroutine for decryption
def decrypt(messageParts):
    # Requests whether the cipher Key is known
    decision = input("\nDo you know what the caeser key is? Y or N\n").upper()
    decryptList = []

    # Decodes if the cipher key is known
    if decision == "Y":
        key = int(input("What to decrypt by: "))

        # decodes according to the key given
        for word in messageParts:
            for j in range(len(word)):
                letter = word[j]
                value = ord(letter)
                if not letter.isalpha():
                    print(letter, end="")
                else:
                    if letter.isupper():
                        if value - key < 65:
                            chrCode = 65 - value + key
                            newChr = 91 - chrCode
                        else:
                            newChr = value - key
                    
                    elif letter.islower():
                        if value - key < 97:
                            chrCode = 97 - value + key
                            newChr = 123 - chrCode
                        else:
                            newChr = value - key
                    print(chr(newChr), end = "")
            print(end=" ")
        
        # Reruns Menu
        print()
        print("#-"*25)
        menu()

    # If the cipher key is unknown, run this:
    elif decision == "N":

        # Decodes each letter and forms it in 3d lists
        for word in messageParts:
            sepWord = []
            for key in range(1,27):
                sepLetter = []
                for j in range(len(word)):
                    letter = word[j]
                    value = ord(letter)
                    if not letter.isalpha():
                        wordValue = letter
                    else:
                        if letter.isupper():
                            if value - key < 65:
                                chrCode = 65 - value + key
                                newChr = 91 - chrCode
                            else:
                                newChr = value - key
                        
                        elif letter.islower():
                            if value - key < 97:
                                chrCode = 97 - value + key
                                newChr = 123 - chrCode
                            else:
                                newChr = value - key
                        wordValue = chr(newChr)
                    sepLetter.append(wordValue)
                sepWord.append(sepLetter)
            decryptList.append(sepWord)
    
        formedList = []

        
        # Recompiles the words from letters and separates them by which word is belongs to in the message and the combination it could be
        for wordSet in decryptList:
            formedWordSet = []
            for word in wordSet:
                formedWord = "".join(word)
                formedWordSet.append(formedWord)
            formedList.append(formedWordSet)

        print("#-"*25)
        print("Possible Sentences:")

        # Returns the recomposed sentences from each possibility
        for check in range(26):
            for i in range(len(messageParts)):
                    print(formedList[i][check], end=" ")
            print()

        # allows for use of the decrypted words in other subroutines
        return formedList

## Defines the subroutine to check against the dictionary
def jsonCheck(fL):
    indexList = []

    # Loads the dictionary for use
    with open("wordlist.json", "r") as f:
        data = json.load(f)

        # Find out the indexes of words from the sentence which exist in the dictionary
        for set in fL:
            for word in set:
                if word.isalpha():
                    if word.lower() in data:
                        indexList.append(set.index(word))
    

    try:
        # finds out which indexes are words in the english dictionary
        modalIndex = mode(indexList)
        print("#-"*25)
        print("Most Likely Sentence is:")

        # prints the most correct sentence
        for i in range(len(fL)):
            print(fL[i][modalIndex], end=" ")
    except StatisticsError:
        print("No Option can be found as a suitable sentence from the english dictionary")
    
## Runs the menu Function to start the program
menu()



