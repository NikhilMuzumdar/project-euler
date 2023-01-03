def isBouncy(n):
    if n < 100:
        return False
    n = str(n)
    result = set([n[i] > n[i+1] for i in range(len(n)-1) if n[i] != n[i+1]])
    return len(result) == 2

def find_limit(target=0.5):
    (start, ratio, count) = (0,0,0)
    while ratio < target:
        start += 1
        if isBouncy(start):
            count += 1
        ratio = count / start
    print(start, ratio)

find_limit(0.99)