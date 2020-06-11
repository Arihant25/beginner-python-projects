alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrypt: ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a positive number to encrypt the message\nor enter a negative number to decrypt your code:"))
encryptedString = ""

for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
            encryptedString = encryptedString + alphabet[newPosition]
    else:
            encryptedString = encryptedString + currentCharacter
print("Your encrypted message is {}".format(encryptedString))
