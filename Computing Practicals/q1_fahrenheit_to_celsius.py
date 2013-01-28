#Name: Python BMI CALCULATHOR.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/24/2013
#Modified: 1/24/2013
#Description: Fahrenheit to Celcius Converter.

print("Welcome to the Fahrenheit to Celcius CONVERTER! :D")

restart="yes"
while restart=="yes":
    print()

    #Input Fahrenheit value
    Fahrenheit= (input("enter Fahrenheit here for conversion!"))

    #Convert Fahrenheit to Celcius
    Celcius= 5/9*(float(Fahrenheit)-32)
    #Display Result
    print('{0:.2f}'.format(Celcius),"degrees(2dp)")

    print()
    restart= input("Do you want to try again(yes/no)?")




