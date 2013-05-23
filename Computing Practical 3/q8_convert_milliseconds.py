#filename: q8_convert_milliseconds.py
#author: Ng Yi Jun Alan (NALA) :D
#note: converts milliseconds to hours, minutes, and seconds

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

def convert_ms(n):
    h=int( int(n) / 3600000 )
    m=int( (int(n)-h*3600000) / 60000 )
    s=int( (int(n)-h*3600000-m*60000) / 1000 )
    conversion=[str(h),str(m),str(s)]
    return(":".join(conversion))

#main
print("Convert milliseconds to hours,minutes and seconds :D") 
restart="yes"
while yesno(restart) == 1:
    print()

    ms= input("Enter millisecond:")
    while not check_int(ms):
        ms = input("Invalid input. millisecond:")
    print(convert_ms(ms))

    print()
    restart = input("do you wish to try again?")
