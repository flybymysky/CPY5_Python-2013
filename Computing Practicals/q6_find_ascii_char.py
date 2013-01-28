#Name: ASCII CODE TO CHARACTER.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/27/2013
#Modified: 1/27/2013
#Description: Find the character of an ASCII code.

print("enter ASCII code to retrieve its character.")

restart="yes"
while restart=="yes":

    #provide ASCII code
    number = input("enter ASCII code (integer, O-127): ")
    print()

    #convert and present ASCII character(s)
    print("ASCII character(s):", chr(int(number)))

    input("do you want to try again? (yes/no)")
