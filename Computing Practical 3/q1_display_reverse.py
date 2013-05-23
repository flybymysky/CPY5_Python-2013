#filename: q1_display_reverse.py
#author: Ng Yi Jun Alan (NALA) :D

def yesno(Input): #yes no inputs
    Y = ['yes','y']
    N = ['no','n']
    if Input.lower() in Y:
        return 1
    elif Input.lower() in N:
        return 0
    else:
        Input = input("Unrecognised input. yes or no:")
        return yesno(Input)

def check_int(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False
    
    
def reverse_int(n):
    absn = str( abs(int(n)) ) #remove negative sign if any
    reverse = absn[::-1]
    if n[0] == "-": #check if negative number
        reverse = "-"+reverse
    return(reverse)

# main
restart = "Y"
while yesno(restart)==1:
    
    Input = input("Enter integer: ")
    while not check_int(Input):
        Input = input("Invalid input. Enter integer: ")
    print(reverse_int(Input))
    print()
    
    restart = input("do you want to try again?")
