#filename: q2_display_pattern.py
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
    
def display_pattern(n):
    length = len(n)-1
    linelength = 2*len(n)-1 #length of n with spaces inbetween
    n = str(int(n)) #remove any zeroes infront
    digits = []
    lines = []
    for i in range(0, length+1):
        digits.append(n[length-i])
        lines.append(" ".join(digits[::-1]).rjust(linelength))
    return "\n".join(lines)

# main
restart = "Y"
while yesno(restart)==1:

    Input = input("Enter integer: ")
    while not check_int(Input):
        Input = input("Invalid integer. Enter integer: ")
    
    print(display_pattern(Input))

    print()
    restart = input("do you want to try again? (yes/no)")
