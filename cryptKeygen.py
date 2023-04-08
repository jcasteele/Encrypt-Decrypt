import os
import random
import sys
import primeFinder
import cryptMath

def main():
    
    filename = input("Enter filename for key generation: ")
    
    print("Creating public and private key files...")
    
    keyFiles(filename, 1024)
    
    print("Keys created and saved in %s_public.txt and %s_private.txt" %(filename, filename))

def keyGen(size):
    
    a = 0
    b = 0
    
    print("Generating prime numbers...")
    
    while a == b:
        a = primeFinder.largePrime(size)
        b = primeFinder.largePrime(size)
    
    c = a * b
    
    print("Calculating...")
    
    while True:
        d = random.randrange(2 ** (size - 1), 2 ** (size))
        
        if cryptMath.greatestCommonDenom(d, (a - 1) * (b - 1) == 1):
            break
    
    e = cryptMath.modInverse(d, (a - 1) * (b - 1))
    
    publicKey = (c, d)
    privateKey = (c, e)
    
    print("Public key: ", publicKey)
    print("Private key: ", privateKey)
    
    return (publicKey, privateKey)

def keyFiles(name, size):
    
    if os.path.exists("%s_public.txt" %(name)) or os.path.exists("%s_private.txt" %(name)):
        userWarn = input("WARNING: Key files named %s_public.txt or %s_private.txt already exist. Continuing will overwrite these files. Do you wish to continue? (Y/N): " %(name, name))
        
        if userWarn != "Y":
            sys.exit("Exiting.")

        publicKey, privateKey = keyGen(size)
    
    print()
    print("Writing public key to file %s_public.txt..." %(name))
    
    writefile = open("%s_public.txt" %(name), "w")
    writefile.write("%s, %s, %s" %(size, publicKey[0], publicKey[1]))
    writefile.close()
    
    print()
    print("Writing private key to file %s_private.txt..." %(name))
    
    writefile = open("%s_private.txt" %(name), "w")
    writefile.write("%s, %s, %s" %(size, privateKey[0], privateKey[1]))
    writefile.close()
        
    return

if __name__ == "__main__":
    main()