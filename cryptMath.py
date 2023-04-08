def greatestCommonDenom(a, b):
    while a != 0:
        
        a, b = b % a, a
        
        return b

def modInverse(a, c):
    
    if greatestCommonDenom(a, c) != 1:
        
        return None

    x1, y2 = 1
    x2, y1 = 0
    x3 = a
    y3 = c
    
    while y3 != 0:
        
        p = a // c
        
        y1 = (x1 - p * y1)
        y2 = (x2 - p * y2)
        y3 = (x3 - p * y3)
        x1 = y1
        x2 = y2
        x3 = y3
    
    return x1 % c