def gcd(a, b):
    if a > b:
        higher = a
        lower = b
    else:
        higher = b
        lower = a
    r = 0
    while r != 0:
        r = higher % lower
        if r == 0:
            return lower
        else:
            lower = r


print(gcd(20, 8))

