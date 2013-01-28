#Name: GENERATE PAYROLL.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/27/2013
#Modified: 1/27/2013
#Description: Generate a payroll.

print("Welcome! You may generate your payroll here.")

restart="yes"
while restart=="yes":
    print()
    
    #provide information
    name = input("enter name: ")
    hours = input("enter no. of hours worked weekly: ")
    payrate = input("enter hourly pay rate: ")
    CPFinput = input("CPF contribution rate(%): ")

    #calculating...
    grosspay = float(hours) * float(payrate)
    CPFoutput = int(CPFinput)/100 * float(grosspay)
    netpay = float(grosspay) - float(CPFoutput)
    print()

    #generate payroll
    print("=====================Payroll=======================")
    print("Payroll statement for", name)
    print("Number of hours worked in week:", hours)
    print("Hourly pay rate: $", '{0:.2f}'.format(float(payrate)))
    print("Gross pay = $", '{0:.2f}'.format(float(grosspay)))
    print("CPF contribution at",CPFinput,"% = $", '{0:.2f}'.format(float(CPFoutput)))
    print()
    print("Net pay = $", '{0:.2f}'.format(float(netpay)))
    
    print()
    restart= input("do you wish to try again? (yes/no)")
