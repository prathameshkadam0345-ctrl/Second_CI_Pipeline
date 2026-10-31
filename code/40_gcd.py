# Program 40: Find GCD of Two Numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
