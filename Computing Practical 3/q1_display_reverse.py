#filename: q1_display_reverse.py
#author: Ng Yi Jun Alan (NALA) :D

def check_int(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False
    
    
def reverse_int(n):
    reverse = 0
    for i in range(0, len(str(n))):
        reverse = reverse*10 + int(n%10)
        n = n//10
    return(reverse)

# main
restart = "yes"
while restart == "yes":
    
    Input = input("Enter integer: ")
    while not check_int(Input):
        Input = input("Enter integer: ")
    print(reverse_int(integer))
    print()
    
    restart = input("do you want to try again? (yes/no)")
