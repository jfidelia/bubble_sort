def gcd(a,b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

print(gcd(30,80))
print(gcd(46,92))
