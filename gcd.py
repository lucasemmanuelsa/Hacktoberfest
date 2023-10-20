def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        a = a-b
        if(b>a):
            if(b % a == 0):
                return a
            else:
                return gcd(a,b)
        else:
            if(a % b == 0):
                return b
            else:
                return gcd(a, b)
    else:
        b = b - a
        if(b>a):
            if(b % a == 0):
                return a
            else:
                return gcd(a,b)
        else:
            if(a % b == 0):
                return b
            else:
                return gcd(a, b)

def gcdOutro(a,b):
    if(a == b):
        return a
    if(a > b):
        return gcd(a-b, b)
    else:
        return gcd(a,b-a)

print(gcd(98,56))

print(gcdOutro(98, 56))