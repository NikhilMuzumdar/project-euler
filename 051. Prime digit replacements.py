def same_digits(n):
    result = True
    digits = sorted(str(n))
    for i in range(2, 7):
        if sorted(str(n*i)) != digits:
            result = False
            break
    return result

n=1
while not same_digits(n):
  n += 1

print(n, end="\n\n")
for i in range(1, 7):
    print(i*n)
