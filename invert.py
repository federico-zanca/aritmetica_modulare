def extended_euclidean_algorithm(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        print(str(a)+"="+str(q)+"*"+str(a)+"+"+str(r))
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x

a = int(input("Enter a: "))
b = int(input("Enter n: "))
d, x = extended_euclidean_algorithm(a, b)
print("gcd("+str(a)+","+str(b)+")="+str(d))
print("x="+str(x)+" inv di "+str(a)+"(mod"+str(b)+")")
