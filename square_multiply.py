def square_multiply(a, b, n):
    ogb = b
    b = bin(b)[2:]
    x = 1
    y = 2
    for i in range(len(b)):
        x = x**2 % n
        if i > 0:
            y = y**2 % n
        if b[i] == '1':
            x = x * a % n
        print(str(b[i])+ " "+str(a)+"^"+str(2**i)+"=" + str(y))
    print("Risultato: \n"+str(a)+"**"+str(ogb)+"(mod "+str(n)+")=")
    return x

def main():
    print("Square and multiply")
    a = int(input("Inserisci a: "))
    b = int(input("Inserisci b: "))
    n = int(input("Inserisci n: "))
    print(square_multiply(a, b, n))

main()