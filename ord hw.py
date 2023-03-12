### Caeser Cipher and Decryptor

decryptList = []
message = input("Type a message to encrypt: ")
key = int(input("What would you like to encrypt by: "))


for i in range(len(message)): 
    print(chr((ord(message[i]) + key)), end = " ")

message = input("\nMessage to Decrypt: ")

decision = input("\nDo you know what the caeser key is? Y or N\n").upper()


if decision == "Y":
    key = int(input("What to decrypt by: "))
    for i in range(len(message)): 
        print(chr((ord(message[i]) - key)), end = " ")
    

elif decision == "N":
    for key in range(1, 27):
        for i in range(len(message)):
            decryptList.append(chr((ord(message[i]) - key)))
            
            print(chr((ord(message[i]) - key)), end = " ")

for i in decryptList:
    with open("wordlist.json", "r") as f:
        json.dump(data, f)
            
