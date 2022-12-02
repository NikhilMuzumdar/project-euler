from math import sqrt, floor

def tri(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def n_factors(n):
    factors = 0
    for i in range(1, floor(sqrt(n))+1 ):
        if n % i == 0:
            if i*i != n:
                factors += 2
            else:
                factors += 1
    return factors

i = 1
while n_factors(tri(i)) <= 500:
    i += 1

print(tri(i))
