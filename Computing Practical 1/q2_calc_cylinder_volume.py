#Name: VOLUME OF A CYLINDER CALCULATHOR.
#Author: Ng Yi Jun Alan (NALA)
#Created: 1/24/2013
#Modified: 1/24/2013
#Description: Compute the volume of a cylinder.

print("Welcome to the cylinder volume CALCULATOR :D")

restart="yes"
while restart=="yes":
    print()
      
    #Provide the radius and length quantities
    radius = input("Key in the Cylinder's Radius:")
    length = input("Key in the Cylinder's Length:")
    
    #Compute the Volume of the cylinder
    volume = '{0:.2f}'.format(22/7*pow(float(radius),2)*float(length))

    #Display Result
    print("volume of cylinder is", volume,"(2dp)")

    print()
    restart=input("do you wish to try again? (yes/no)")


