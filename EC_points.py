print("a = ", end='')
a = int(input())
print("b = ", end='')
b = int(input())
print("p = ", end='')
p = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def legendre(a, p):
    return (a**((p-1)//2))%p

def sqrt_mod(a, p):
    if p%4 == 3:
        return a**((p+1)//4)%p
    elif p%4 == 1:
        print("dunno")
        exit()

def ell_points_brute(a, b, p):
    n = 1
    for x in range(p):
        for y in range(p):
            if (y**2)%p == (x**3 + a*x + b)%p:
                print("("+str(x)+", "+str(y)+")")
                n+=1
    print("O")
    return n
def ell_points(a, b, p):
    n = 1
    for x in range(p):
        y2 = (x**3 + a*x + b)%p
        if legendre(y2, p) == 1:
            y = sqrt_mod(y2, p)
            print("("+str(x)+", "+str(y)+")")
            print("("+str(x)+", "+str(p-y)+")")
            n+=2
        elif(legendre(y2, p) == 0):
            print("("+str(x)+", 0)")
            n+=1
    print("O")
    return n
n = ell_points(a, b, p)
print("n = ", n)