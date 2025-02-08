from fractions import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]