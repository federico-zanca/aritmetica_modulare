n = int(input("Enter n: "))

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

p_1 = n-1
s = 0
while((p_1)%2 == 0):
    p_1 = p_1//2
    s+=1

d = (n-1)//(2**s)
print("d: ", d)
print("s: ", s)
print("n-1 = ", n-1, " = 2^", s, "*", d)

for a in range(2, n):
    x = (a**d)%n
    print("a: ", a, " x: a**d mod n=", x)
    if x%n == 1 or x%n == n-1:
        continue
    else:
        r = 1
        while(r<s and x != n-1):
            x = (x**2)%n
            print("x: ",x,"^2 mod n=", x)
            r+=1
            if x%n == 1:
                print("Composite")
                break
    
