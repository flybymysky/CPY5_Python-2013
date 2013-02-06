#Name: CHECK INTEGER FOR EVEN OR ODD.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/6/2013
#Modified: 2/6/2013
#Description: Check if integer is even or odd.

print("Check for even or odd for Integer! :D")

restart="yes"
while restart=="yes":
    print()

    #Input Integer
    Integer= int(input("enter your Integer!"))

    #Check Even or Odd
    if Integer%2 ==1:
        print(Integer,"is odd")
    else:
        print(Integer,"is even")

    print()
    restart= input("Do you want to try again(yes/no)?")




