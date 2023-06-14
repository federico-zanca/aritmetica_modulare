import math
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
    n = int(math.ceil(math.sqrt(p - 1)))
    print(str(alfa) + "**x (mod " + str(p) + ") == " + str(beta))
    print("Riscrivo x in base N \nN=ceil(sqrt("+str(p-1)+"))="+str(n))
    print("jk\t a**j\t b*a**(-N*k)")
    j_values = []
    k_values = []
    for j in range(n):
        alfa_j = pow(alfa, j, p)
        j_values.append(alfa_j)
        beta_alfa_nk = (beta * pow(alfa, -n*j, p)) % p
        k_values.append(beta_alfa_nk)
        print(str(j)+"\t "+str(alfa_j)+"\t "+str(beta_alfa_nk))
        if(beta_alfa_nk in j_values):
            print("x = j"+" + "+str(n)+"k")
            print("j="+str(j_values.index(beta_alfa_nk))+", k="+str(k_values.index(beta_alfa_nk)))
            return j + n * k_values.index(beta_alfa_nk)
        elif(alfa_j in k_values):
            print("x = j"+" + "+str(n)+"k")
            print("j="+str(j)+", k="+str(k_values.index(alfa_j)))
            return j + n * k_values.index(alfa_j)

print("Enter alfa**x == beta (mod p)")
alfa = int(input("Enter alfa: "))
beta = int(input("Enter beta: "))
p = int(input("Enter p: "))
print("x="+str(babystep_giantstep(alfa, beta, p)))