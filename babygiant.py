import math

def babystep_giantstep(alfa, beta, p):
    n = int(math.ceil(math.sqrt(p - 1)))
    print(str(alfa) + "**x (mod " + str(p) + ") == " + str(beta))
    print("Riscrivo x in base \nN=ceil(sqrt("+str(p-1)+"))="+str(n))
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