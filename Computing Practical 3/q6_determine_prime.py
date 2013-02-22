#filename: q6_determine_prime.py
#author: Ng Yi Jun Alan (NALA) :D

def is_prime(n):
    prime=True
    for i in range(2,n):
        if n%i ==0:
            prime=False
            break
    return(prime)

primes = []
x=2
while len(primes)<= 1000:
    if is_prime(x)==True:
        primes.append(str(x).ljust(4))
        x=x+1
    else:
        x=x+1

a=0
b=10
while b<=1000:
    print(" ".join(primes[a:b]))
    a=a+10
    b=b+10
