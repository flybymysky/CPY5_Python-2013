#filename: q4_sum_series.py
#author: Ng Yi Jun Alan (NALA) :D

def m_series(i):
    n=1 #n is short for numerator
    d=2 #d is short for denominator
    result=0
    while n<=i and d<=i+1:
        result=result+n/d
        n=n+1
        d=d+1
    return(result)

#main
print("i"+"m(i)".rjust(9))
a=0
for x in range(1,21):
    print('{0:<5}'.format(x),'{0:<10.4f}'.format(m_series(1+a)))
    a=a+1
