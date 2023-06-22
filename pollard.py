def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard(n):
    a = 2
    b = 2
    d=1
    i=2
    print("b1=2 mod "+str(n))
    while(True):
        old = b
        b = b**i%n
        d = gcd(b-1, n)
        print("b"+str(i)+"="+str(old)+"^"+str(i)+"="+str(b))
        print("MCD("+str(b)+"-1,"+str(n)+")="+str(d))
        i+=1
        if d != 1:
            return d

n = int(input("Enter n: "))
factor = pollard(n)
print("Factors:", factor, n // factor)
