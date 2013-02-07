#Name: KILOGRAMS TO POUNDS TABLE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/5/2013
#Description: Kilograms to Pounds Table.

print("The Kilograms to Pounds Chart.")
print()

#Print Table
print("Kilograms Pounds")
pounds = 0
for kilograms in range(1,11):
    pounds = pounds + 2.2
    print('{0:<9}'.format(kilograms), '{0:<.1f}'.format(pounds))

print()
input("Press enter to exit.")




