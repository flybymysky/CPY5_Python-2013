#filename = q3_find_gcd.py
#author= Ng Yi Jun Alan (NALA) :D

def gcd(m,n):
    if m>n:
        d=n
    elif n>m:
        d=m
    else:
        d=m
    while m%d != 0 or n%d !=0:
            d=d-1
    print(d)

#main
print("for gcd(24,16):")
gcd(24,16)
print("for gcd(255,25):")
gcd(255,25)
