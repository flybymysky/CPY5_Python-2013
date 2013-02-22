#filename: q5_compute_series.py
#author: Ng Yi Jun Alan (NALA):D

def m(i):
    a = 1
    answer = 0
    while a<=i:
        answer= answer + 1/(2*a-1) - 1/(2*a+1)
        a=a+2
    answer = 4*answer
    return(answer)

#main
print("i     m(i)")
for x in range(1,20,2):
    print('{0:<5}'.format(x),'{0:<10.11f}'.format(m(x)))
