'''
It's method for identify prime numbers
'''
def isPrime(m):
    if type(m) != int or m<2:
        return False;
    if m in [2,3,5,7,11,13,17]:
        return True;
    if m%2==0:
        return False;
    d=3;
    while d*d<=m:
        if m % d == 0:
            return False;
        d +=2;
    return True;

'''Resheto Eratosfena '''
def sieve(n):
    primes=[];
    for i in range(n):
        primes.append(True)
    primes[0] = False
    primes[1] = False
    p = 2
    while p*p <n:
        #check out all multiples of p
        #starting from p*p
        i=p*p;
        while i < n:
            primes[i]=False
            i +=p
          #Search for the first unchecked number
        p+=1
    #end while p*p < n
    res = []
    for i in range(n):
        if primes[i]:
            res.append(i)
    return res
