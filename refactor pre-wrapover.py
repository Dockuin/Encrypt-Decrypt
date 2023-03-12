### ORD & CHR HOMEWORK REFACTORED

# imports libraries for use (json to read a json file and stats to find the modal value of a list)
import json
from statistics import mode


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
            print(chr((ord(word[j]) + key)), end = "")
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
                print(chr((ord(word[j]) - key)), end = "")
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
                    wordValue = chr((ord(word[j]) - key))
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
        for j in range(len(formedList)):
            for i in range(len(messageParts)):
                print(formedList[i][j], end=" ")
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
                if word in data:
                    indexList.append(set.index(word))
    
    # finds out which indexes are words in the english dictionary
    modalIndex = mode(indexList)
    print("#-"*25)
    print("Most Likely Sentence is:")

    # prints the most correct sentence
    for i in range(len(fL)):
        print(fL[i][modalIndex], end=" ")
    
## Runs the menu Function to start the program
menu()





### EXTRA LIMITING TASK
# Excludes symbols as they will not be encrypted (if they were to be used  a range from 33 to 123)

# 65-90
# 97-122

letter = "a"
key = 2


value = ord(letter)
test2 = value + key

# encrypt

# if value + key > 90 or value + key > 122:
#     if letter.isupper():
#         test1 = value + key - 90
#         test2 = 64 + test1
    
#     elif letter.islower():
#         test1 = value + key - 122
#         test2 = 96 + test1




# decrypt
if value - key < 65 or value - key < 97:
    if letter.isupper():
        test1 = 65 - value + key
        test2 = 91 - test1
    elif letter.islower():
        test1 = 97 - value + key
        test2 = 123 - test1

    

print(chr(test2))



