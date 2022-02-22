import random
numpad = int(input('please input a number '))
message = "I WENT TO THE BEACH"
encryptedmessage = ""

def generatepad(numpad):
    #specifying length of message
    newnumpad = []
    for num in range(numpad):
        shifts = random.randint(65, 91)
        newnumpad.append(shifts)
    print('newnumpad is: ', newnumpad)
    return newnumpad

def encipher(newnumpad, encryptedmessage):
    encryptedmessage = ""
    j = 0
    for ch in message: 
        ch = ord(ch)
        if ch in range(65,91):
            ch = (ch - 65 + newnumpad[j]) % 26 + 65
        else: 
            ch = ch
        ch = chr(ch)
        encryptedmessage = encryptedmessage + ch
        j += 1
    print('encryptedmessage:' , encryptedmessage)
    return encryptedmessage


def decipher(newnumpad, encryptedmessage):
   decryptedmessage = ""
   i = 0
   for character in encryptedmessage: 
       character = ord(character)
       if character in range(65, 91):
        character = (character - 65 - newnumpad[i]) % 26 + 65
       else: 
           character = character
       character = chr(character)
       decryptedmessage = decryptedmessage + character
       i += 1
   print('decrypted message: ', decryptedmessage)



#open pad.txt and read it, create a newnumpad for pad.txt, open encryptedmessage.txt, run encrypted message through decipher using pad.txt's newnumpad. once decrypted, write the result to decrypted-message.txt. 

with open('pad.txt') as file: 
    pad = file.read()


g = open('encryptedmessage.txt', 'r')
answer = decipher(g, newnumpad)
answer = open('decrypted-message', 'w')


generatepad()  
encryption = encipher(encryptedmessage)
decipher(encryption)
