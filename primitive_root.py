def invert(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x

def pow(a, b, n):
    ogb = b
    if(b<0):
        b = -b
        a = invert(a, n)
    b = bin(b)[2:]
    x = 1
    y = a
    for i in range(len(b)):
        x = x**2 % n
        if i > 0:
            y = y**2 % n
        if b[i] == '1':
            x = x * a % n
    return x

def prime_factors(n):
    print("Prime factors of "+str(n)+":")
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    print(factors)
    return factors

def is_primitive_root(a, p):
    if a == 1:
        print("a = 1")
        return False
    result = pow(a, p - 1, p)
    if result != 1:
        print(str(a) + "**" + str(p - 1) + "(mod " + str(p) + ") == "+str(result))
        return False
    for q in prime_factors(p - 1):
        result = pow(a, (p - 1) // q, p)
        print(str(a) + "**" + str((p - 1) // q) + "(mod " + str(p) + ") == "+str(result))
        if result == 1:
            return False
    return True

a = int(input("Enter a: "))
p = int(input("Enter p: "))
print(is_primitive_root(a, p))