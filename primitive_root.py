def prime_factors(n):
    print("Prime factors of "+str(n)+":")
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    print(factors)
    return factors

def is_primitive_root(a, p):
    if a == 1:
        print("a = 1")
        return False
    result = pow(a, p - 1, p)
    if result != 1:
        print(str(a) + "**" + str(p - 1) + "(mod " + str(p) + ") == "+str(result))
        return False
    for q in prime_factors(p - 1):
        result = pow(a, (p - 1) // q, p)
        print(str(a) + "**" + str((p - 1) // q) + "(mod " + str(p) + ") == "+str(result))
        if result == 1:
            return False
    return True

a = int(input("Enter a: "))
p = int(input("Enter p: "))
print(is_primitive_root(a, p))