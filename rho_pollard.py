def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard(n):
    x = 2
    i = 0
    y = x
    d = 1
    print("i    x    y      d")
    print("     xi  2xi  gcd(|x-y|,n)")
    print("0    2    2       1")
    while d == 1:
        x = (x**2 + 1) % n

        y = (y**2 + 1) % n
        y = (y**2 + 1) % n

        d = gcd(abs(x - y), n)
        i+=1
        print(str(i)+(4-len(str(i))+1)*" "+str(x)+(4-len(str(x))+1)*" "+str(y)+(4-len(str(d))+2)*" "+str(d))        
    q = d
    p = n //q
    print("q:", q)
    print("p:", p)

n = int(input("Enter n: "))
print("f(x)=x^2+1\nwalking funct")
print("start from x0=2")
pollard(n)

