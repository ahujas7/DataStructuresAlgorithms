# Finding the greatest common denominator of two numbers

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % a
    return a
