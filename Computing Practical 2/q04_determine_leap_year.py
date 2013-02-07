#Name: LEAP YEAR DETERMINOR
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/24/2013
#Modified: 1/24/2013
#Description: Determine if year is leap year.

print("Determine if Year is a Leap Year here!")

restart="yes"
while restart=="yes":
    print()

    #Input Year
    Year= int(input("enter Year!"))

    #Print if Leap Year or not
    if Year%4==0:
        print(Year, "is leap year.")
    else:
        print(Year, "is not a leap year.")
    
    print()
    restart= input("Do you want to try again(yes/no)?")




