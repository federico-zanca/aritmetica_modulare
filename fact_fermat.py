import math

def is_square(n):
    return math.sqrt(n)%1 == 0

def fermat_factor(n):
    i=1
    while(True):
        a = n+i**2
        print("n + %s = %s" % (i**2, a))
        if is_square(a):
            radice = math.sqrt(a)
            factors = (int(radice) - i, int(radice) + i)
            print("Factors are", factors)
            break
        i+=1
while True:
    try:
        n = int(input("Enter n: "))
        if n <= 0:
            print("Negative integer!")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

fermat_factor(n)