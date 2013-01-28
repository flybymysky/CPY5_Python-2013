#Name: MILES TO KILOMETRES CONVERTER.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/24/2013
#Modified: 1/24/2013
#Description: Miles to Kilometres CONVERTER.

print("Welcome to the Miles to Kilometres CONVERTER :D")

restart="yes"
while restart=="yes":
    print()
    
    #input Miles
    Miles= input("provide the number of miles:")

    #convert Miles to Kilometres
    Kilometres= '{0:.3f}'.format(float(Miles)*1.60934)

    #display Results
    print(Kilometres, "km (3dp)")

    print()
    restart=input("do you wish to try again? (yes/no)")
