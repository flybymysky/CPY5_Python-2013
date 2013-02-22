#filename: q7_display_matrix.py
#author: Ng Yi Jun Alan (NALA) :D

import random

def print_matrix(n):
    height=0
    while height<n:
        matrix =[]
        length=0
        while length<n:
            matrix.append(str(random.randint(0, 1)))
            length=length+1 
        print(" ".join(matrix))
        height=height+1

#main
restart="yes"
while restart=="yes":
    print()
    
    integer=int(input("enter integer for matrix:"))
    print_matrix(integer)

    print()
    restart=input("do you wish to try again? (yes/no):")
