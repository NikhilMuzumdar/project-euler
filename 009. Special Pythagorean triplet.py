import math

ps = [number**2 for number in range(2, 600+2+1)]

# Find Triplets
for i in ps:
    for j in ps:
        if i < j:
            k = i + j
            if k in ps:
                a = math.sqrt(i)
                b = math.sqrt(j)
                c = math.sqrt(k)
                if a+b+c == 1000:
                    print(a*b*c)
