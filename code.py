# this is just a fun project you can use it for whatever

import string
import re

#List Of Upper Case Letters For Cipher
A = list(string.ascii_uppercase)
Cipher = []

#To Decrypt Or Encrypt
Flag = input("To Encrypt Enter 1 to Decrypt Enter 0: ")

while(True):
    Key = int(input("Please Enter a Key Between 1 and 25: "))
    #Verfication Of Key
    if(Key < 26):
        break

#If we want to decrypt we'll need the Kbar which satisfies K + KBAR = 26 
if(Flag == '0'): Key = 26 - Key

S = input("Please Enter Plaintext: ")

#remove spaces and special characters using regular expression
CleanString = re.sub('\W+','',S)

for x in range(0,len(CleanString)):
    temp = 0
    Position = A.index(CleanString[x].upper())
    Ceaser = (Position+Key) % 26
    Cipher.append(A[Ceaser])

#To Decrypt You can use K-bar instead of Key and print
print(''.join(Cipher))
