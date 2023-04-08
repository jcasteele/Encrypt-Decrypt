import math
import random

def primeDivide(num):
    if num < 2:
        return False
    for p in range(2, int(math.sqrt(num)) + 1):
        if num % p == 0:
            return False
        
    return True

def primeSieve(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False

    for s in range(2, int(math.sqrt(size)) + 1):
        check = s * 2
        primeArray = [] 
        
        while(check < size):
            sieve[check] == False
            check += 1          
        
        for f in range(size):
            if sieve[f] == True:
                primeArray.append(f)
    
    return primeArray
                
def primeMillerRabin(num):
    x = num - 1
    y = 0
    
    if num % 2 == 0:
        return False
    
    if num < 2:
        return False
    
    if num == 3:
        return True
    
    while x % 2 == 0:
        x = x // 2
        y += 1
        
    for test in range(5):
        n = random.randrange(2, num - 1)
        q = pow(n, x, num)
        
        if q != 1:
            r = 0
            
            while q != (num - 1):
                if r == y:
                    return False
                else:
                    r = r + 1
                    q = (q ** 2) % num
                    
    return True

low_primes = primeSieve(100)

def isPrime(num):
    if (num < 2):
        return False
    
    for prime in low_primes:
        if (num % prime == 0):
            return False
    
    return primeMillerRabin(num)

def largePrime(key = 1024):
    while True:
        num = random.randrange(2 ** (key - 1), 2 ** (key))
    
        if isPrime(num):
            return num