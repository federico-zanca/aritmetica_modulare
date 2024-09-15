print("a: ", end='')
a = int(input())
print("n: ", end='')
n = int(input())

u = [n, 1, 0]

v = [a%n, 0, 1]
w = [7 ,7, 7]

i = 0
while(w[0]!=0):
    print("Iteration ", i)
    print("u: ", u)
    print("v: ", v)
    i+=1
    
    q = u[0]//v[0]

    w[0] = u[0]-(q*v[0])
    w[1] = u[1]-(q*v[1])
    w[2] = u[2]-(q*v[2])
    
    print("q: ", q)
    print("w: ", w)

    u = [x for x in v]
    v = [x for x in w]

print("gcd: ", u[0])
print("other: ", u[1])
print("inverso: ", u[2], "-> ", u[2]%n)


