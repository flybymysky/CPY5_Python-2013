#Name: MILES TO KILOMETRES TABLE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/5/2013
#Description: Miles to Kilometres Chart.

print("The Miles <-> Kilometres Chart.")
print()

#Print Table
print("Miles Kilometres Kilometres Miles")
kmA = -1.609
kmB = 20
milesB = 1/1.609
for milesA in range(1,11):
    kmA = kmA + 1.609
    kmB = kmB + 5
    if milesA<7:
        print(milesA, '{0:>9.3f}'.format(kmA+1.609), '{0:>7}'.format(kmB-5), '{0:>14.3f}'.format(milesB*(kmB-5)))
    elif milesA<10:
        print(milesA, '{0:>10.3f}'.format(kmA+1.609), '{0:>6}'.format(kmB-5), '{0:>14.3f}'.format(milesB*(kmB-5)))
    elif milesA==10:
        print(milesA, '{0:>9.3f}'.format(kmA+1.609), '{0:>6}'.format(kmB-5), '{0:>14.3f}'.format(milesB*(kmB-5)))

print()
input("Press enter to exit.")


