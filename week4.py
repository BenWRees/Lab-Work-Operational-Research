import math
#test whether a number is prime - PART 1
def isprime(n):
    if n >= 2:
        for i in range(2,int(math.floor(math.sqrt(n)+1))):
            if ( n % i == 0):
                return False
        return True

#find the first value for
def wrong_prime() :
    p=1
    while(True) :
        if(isprime(p)) :
            if not(isprime((2**p)-1)) :
                return p
        p=p+1

def mersenne_prime(n_max) :
    list_of_primes = list()
    for p in range(1,n_max) :
        if(isprime(p)) :
            if(isprime((2**p)-1)) :
                list_of_primes.append((2**p)-1)
    return list_of_primes


