def blumblumshub(n, seed):
    first = seed**2 % n
    x = seed
    i=0
    print("Tutto mod "+str(n))
    print("i  x    x**2\tbit")
    while True:
        y = x**2 % n
        print (str(i)+" "+str(x)+"**2="+str(y)+"\t"+str(y%2))
        x = y
        i+=1
        if x == first and i>1:
            return i-1
        
n = int(input("Enter n: "))
seed = int(input("Enter seed: "))
print("Periodo: "+str(blumblumshub(n, seed)))

