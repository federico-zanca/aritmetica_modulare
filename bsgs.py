def invert(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x

def gcd(x,y):
    while y != 0:
        x, y = y, x % y
    return x

def eulero_totient(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result+=1
    return result

def ceiling(x):
    if x == int(x):
        return int(x)
    return int(x)+1

print("g**x=b mod n")
g = int(input("Enter g: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))

original_n = n
phi = eulero_totient(n)
print("phi(n): ", phi)
m = ceiling(phi**0.5)

print("m: ", m)

g_inv = invert(g, original_n)
g_m = ((g_inv%original_n)**m)%original_n
print("g^-m: ", g_m)
baby = []
for j in range(0, m+1):
    baby.append((g**j)%n)

print()

y = b
print("Baby steps:")
print("j    g^j")
for j in range(0, m):
    print(j, "  ", baby[j])
print()
print("Giant steps:")
print("i    b*(g^-m)^i")
for i in range(0, m):
    print(i, "      ", y)
    if y in baby:
        j = baby.index(y)
        break
    y = (y*g_m)%n
print()
print("i: ", i)
print("j: ", j)
print("x= i*m + j =\n", i*m+j)
