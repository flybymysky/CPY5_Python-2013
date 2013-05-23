#filename: q6_determine_prime.py
#author: Ng Yi Jun Alan (NALA) :D

def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

primes = []
x=2
while len(primes)<= 1000:
    if is_prime(x)==True:
        primes.append(str(x).ljust(4))
    x=x+1

start=0
end=10
while end<=1000:
    print(" ".join(primes[start:end]))
    start=start+10
    end=end+10
