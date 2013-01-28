#Name: CONVERT LOWERCASE LETTER TO UPPERCASE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/27/2013
#Modified: 1/27/2013
#Description: Convert a lower case letter to its upper case with its ASCII code.

print("Type in any lower case letter to get the upper case through ASCII")
restart="yes"
while restart=="yes":

    print()
    print("(letters in uppercase will return the same. Only for lower case.)")

    #Input Letter
    letter= input("enter letter in lower case:").lower()

    #Convert and display result
    if len(letter) == 1:
        print(chr(int(ord(letter))- 32))

    else:
        print ("error, only 1 letter supported.")

    print()
    restart=input("do you wish to try again? (yes/no)")
