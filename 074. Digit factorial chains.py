import math
import time

s = time.time()

def factorial_sum(number):
    factorial_sum = 0
    number = str(number)
    for d in number:
        factorial_sum += math.factorial(int(d))

    # print(factorial_sum)
    return factorial_sum

def n_cycles(number):
    factorial_sums = [number]
    while factorial_sum(number) not in factorial_sums:
        number = factorial_sum(number)
        factorial_sums.append(number)
    return len(factorial_sums)

i = 1
count = 0
while i < 1000000+1:
    if n_cycles(i) == 60:
        count += 1
    i += 1

print(count)

e = time.time()

print(f"Took {e-s:.2f} seconds to compute!")
