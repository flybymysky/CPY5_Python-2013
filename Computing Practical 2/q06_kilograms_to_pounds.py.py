#Name: KILOGRAMS TO POUNDS TABLE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/5/2013
#Description: Kilograms to Pounds Table.

print("The Kilograms to Pounds Chart.")
print()

#Print Table
print("Kilograms Pounds")
pounds = -2.2
for kilograms in range(1,11):
    pounds = pounds + 2.2
    if pounds<8:
        print(kilograms, '{0:>11.1f}'.format(pounds+2.2))
    elif pounds<19:
        print(kilograms, '{0:>12.1f}'.format(pounds+2.2))
    elif pounds>19:
        print(kilograms, '{0:>11.1f}'.format(pounds+2.2))

print()
input("Press enter to exit.")




