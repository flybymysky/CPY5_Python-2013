#Name: FIND THE LARGEST n for n**3 < 12000.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/5/2013
#Description: Finding the largest n such that n**3 < 12000.

print("The largest n for n^3 smaller than 12000 is...")

#Calculate Largest n
n=1
while n**3 < 12000:
    n=n+1
    
#Print Largest n
print(n-1)

print()
input("press enter to end")




