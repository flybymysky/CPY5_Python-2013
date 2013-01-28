
name = input("enter name: ")
hours = input("enter no. of hours worked weekly: ")
payrate = input("enter hourly pay rate: ")
CPFinput = input("CPF contribution rate(%): ")

grosspay = float(hours) * float(payrate)
CPFoutput = int(CPFinput)/100 * float(grosspay)
netpay = float(grosspay) - float(CPFoutput)
print()

#display results
print("=====================Payroll=======================")
print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: $", '{0:.2f}'.format(float(payrate)))
print("Gross pay = $", '{0:.2f}'.format(float(grosspay)))
print("CPF contribution at",CPFinput,"% = $", '{0:.2f}'.format(float(CPFoutput)))
print()
print("Net pay = $", '{0:.2f}'.format(float(netpay)))
