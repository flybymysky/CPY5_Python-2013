#Name: SMALLEST FACTORS OF AN INTEGER.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/6/2013
#Modified: 2/6/2013
#Description: Find smallest factors of an integer.

print("Input integer to find its smallest factors!")

restart="yes"
while restart=="yes":
    print()

    #Input Integer
    Integer = int(input("Input Integer:"))

    factor = 2
    factors = []
    IntegerA= Integer

    #Solve Factors
    while factor < Integer:
        if IntegerA%factor==0:
            factors.append(factor)
            IntegerA = IntegerA/factor
        else:
            factor=factor+1
    
    #Print Factors
    if len(factors) == 0:
        print(Integer)
    else:
        print(factors)

    print()
    restart=input("do you want to try again? (yes/no)")

    


