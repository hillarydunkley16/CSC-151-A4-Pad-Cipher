import random
numpad = int(input('please input a number '))
message = "I WENT TO THE BEACH"
encryptedmessage = ""
newnumpad = []
padfile = ""
def generatepad(numpad):
    #specifying length of message
    newnumpad = []
    for num in range(numpad):
        shifts = random.randint(65, 91)
        newnumpad.append(shifts)
    print('newnumpad is: ', newnumpad)
    return newnumpad

def encipher(newnumpad, encryptedmessage, padfile):
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
   #print(encryptedmessage)
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
def generatepadfile(fname, len):
    pad = generatepad(len)
    file = open(fname, "w")
    file.write(pad)
    file.close()

generatepadfile("pad.txt", 1200)
with open('pad.txt') as file: 
    pad = file.read()
with open("encrypted-message.txt", "w") as file: 
    file.write(encipher(newnumpad, encryptedmessage, padfile))
with open("encrypted-message.txt") as file:
    text = file.read()
print(decipher(newnumpad, encryptedmessage))


#g = open('encryptedmessage.txt', 'r')
#answer = decipher(g, newnumpad)
#answer = open('decrypted-message', 'w')

#this is a test 
generatepad(numpad)  
encipher(encryptedmessage)
decipher(encryptedmessage)
