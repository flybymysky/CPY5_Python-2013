#Name: TRIANGLE PERIMETER CALCULATHOR.
#Author: Ng Yi Jun Alan (NALA)
#Created: 6/2/2013
#Modified: 6/2/2013
#Description: Perimeter of Triangle Calculathor.

print("Welcome to the Fahrenheit to Celcius CONVERTER! :D")

restart="yes"
while restart=="yes":
    print()

    #Input Sides of Triangle
    SideA= int(input("enter length of first side:"))
    SideB= int(input("enter length of second side:"))
    SideC= int(input("enter length of third side:"))
    print()
    
    #If valid Triangle, print Perimeter
    if SideA + SideB > SideC:
        print("perimeter:",SideA+SideB+SideC)
    else:
        print("Invalid Triangle!")

    print()
    restart= input("Do you want to try again(yes/no)?")




