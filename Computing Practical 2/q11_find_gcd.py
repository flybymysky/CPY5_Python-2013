#Name: GREATEST COMMON DIVISOR OF 2 INTEGERS.
#Author: Ng Yi Jun Alan (NALA)
#Created: 6/2/2013
#Modified: 6/2/2013
#Description: Find the greatest common divisor of 2 integers.

print("Enter 2 Integers to find their greatest common divisor!")


restart="yes"
while restart=="yes":
    print()

    #Input Integers
    IntegerA = int(input("Integer 1:"))
    IntegerB = int(input("Integer 2:"))
    print()
    
    #Retrieve GCD
    if IntegerA>IntegerB:
        d=IntegerB
    elif IntegerB>IntegerA:
        d=IntegerA
    else:
        d=IntegerA
    
    while IntegerA%d != 0 or IntegerB%d !=0:
            d=d-1

    #Print GCD
    print("The Greatest Common Dviisor is",d)


    print()
    restart= input("Do you want to try again(yes/no)?")




