from math import comb

def greater_than_Mn(n,c):
    return comb(n,c) > 1000000

count = 0
for n in range(101):
    for c in range(1, n+1):
        if greater_than_Mn(n, c):
            count += 1
print(count)