#Name: SUM OF DIGITS.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/27/2013
#Modified: 1/27/2013
#Description: Calculate sum of digits in integer.

print("Here you can get the sum of the digits of any integer :D")

restart = "yes"
while restart=="yes":
    print()
    
    #Provide Integer
    integer = int(input("enter integer:"))

    #Calculate sum of digits
    sumofdigits = 0
    while integer > 0:
        sumofdigits = sumofdigits + integer%10
        frontnumbers = integer//10
        integer = frontnumbers

    #Present Result
    print("sum of digits:",sumofdigits)

    print()
    restart=input("Do you wish to try again? (yes/no)")

    

