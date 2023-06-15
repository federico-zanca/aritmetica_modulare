def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
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
def fermat_test(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for a in range(2, n):
        if(gcd(a, n) != 1):
            continue
        result = pow(a, n - 1, n)
        if result != 1:
            print(str(a) + "**" + str(n - 1) + "(mod " + str(n) + ") == "+str(result))
            return False
    return True
n = int(input("Enter n: "))
if(fermat_test(n)):
    print("Fermat Prime")
else:
    print("Not Fermat Prime")