#Name: MILES TO KILOMETRES TABLE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/6/2013
#Description: Miles to Kilometres Chart.

print("The Miles <-> Kilometres Chart.")
print()

#Print Table
print("Miles Kilometres Kilometres Miles")

for milesA in range(1,11):
    kmA = milesA * 1.609
    kmB = 5 *(milesA+3)
    milesB = kmB / 1.609
    
    print('{0:<5}'.format(milesA), '{0:<10.3f}'.format(kmA), '{0:<10}'.format(kmB), '{0:<14.3f}'.format(milesB))

print()
input("Press enter to exit.")


