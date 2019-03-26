def cuboid_volume( a , b , c ) :
    return (a*b*c)

print(cuboid_volume(2,2,2))

#Part 2
def wrong_prime() :
    for p in range(2,100) :
        while(isprime(p) == True) :
            q=(2**p)-1
            if(isprime(q) == False) :
                return q
print(wrong_prime())


print(isprime(0))
print(isprime(1))
print(isprime(4))
print(isprime(6))
print(isprime(9))
print(isprime(2))
print(isprime(3))
print(isprime(5))
print(isprime(7))
print(isprime(11))
print(isprime(13))
print(isprime(17))
print(isprime(47))
print(isprime(101))
print(isprime(2**(19-1)))
