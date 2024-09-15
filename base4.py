# converts from base 10 to base 4
print("n base 10: ", end ='')
n = int(input())

res = ""
while(n > 0):
    res = str(n%4)+res
    n //=4
print("base 4: ",res)