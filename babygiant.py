import math
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_primitive_root(a, p):
    if a == 1:
        return False
    result = pow(a, p - 1, p)
    if result != 1:
        return False
    for q in prime_factors(p - 1):
        result = pow(a, (p - 1) // q, p)
        if result == 1:
            return False
    return True
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

def babystep_giantstep(alfa, beta, p):
    flag = is_primitive_root(alfa, p)
    n = int(math.ceil(math.sqrt(p - 1)))
    print(str(alfa) + "**x (mod " + str(p) + ") == " + str(beta))
    print("Riscrivo x in base N \nN=ceil(sqrt("+str(p-1)+"))="+str(n))
    print("jk\t a**j\t b*a**(-N*k)")
    j_values = []
    k_values = []
    scelti = []
    for j in range(n):
        alfa_j = pow(alfa, j, p)
        j_values.append(alfa_j)
        beta_alfa_nk = (beta * pow(alfa, -n*j, p)) % p
        k_values.append(beta_alfa_nk)
        print(str(j)+"\t "+str(alfa_j)+"\t "+str(beta_alfa_nk))
        if(beta_alfa_nk in j_values):
            #scelti.append([j, k_values.index(beta_alfa_nk)])
            scelti.append([j_values.index(beta_alfa_nk), j])
            if(flag):
                break
            #print("x = j"+" + "+str(n)+"k")
            #print("j="+str(j_values.index(beta_alfa_nk))+", k="+str(k_values.index(beta_alfa_nk)))
            #return j + n * k_values.index(beta_alfa_nk)
        elif(alfa_j in k_values):
            scelti.append([j, k_values.index(alfa_j)])
            if(flag):
                break
            #print("x = j"+" + "+str(n)+"k")
            #print("j="+str(j)+", k="+str(k_values.index(alfa_j)))
            #return j + n * k_values.index(alfa_j)
    print("x = j"+" + "+str(n)+"k")
    for i in range(len(scelti)):
        j= scelti[i][0]
        k= scelti[i][1]
        print("j="+str(j)+", k="+str(k))
        print("x"+str(i)+"="+str(j+n*k))
print("Enter alfa**x == beta (mod p)")
alfa = int(input("Enter alfa: "))
beta = int(input("Enter beta: "))
p = int(input("Enter p: "))
(babystep_giantstep(alfa, beta, p))