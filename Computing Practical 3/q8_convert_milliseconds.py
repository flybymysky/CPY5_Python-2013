#filename: q8_convert_milliseconds.py
#author: Ng Yi Jun Alan (NALA) :D
#note: converts milliseconds to hours, minutes, and seconds

def convert_ms(n):
    h=int( int(n) / 3600000 )
    m=int( (int(n)-h*3600000) / 60000 )
    s=int( (int(n)-h*3600000-m*60000) / 1000 )
    conversion=[str(h),str(m),str(s)]
    return(":".join(conversion))

#main
print("Convert milliseconds to hours,minutes and seconds :D") 
restart="yes"
while restart == "yes":
    print()

    ms= input("Enter milllisecond:")
    print(convert_ms(ms))

    print()
    restart = input("do you wish to try again? yes/no:")
