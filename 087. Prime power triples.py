# Takes time to compute, may not be the efficient way to solve this 

def is_prime(number):
    import math
    result = True
    if number == 2:
        return result
    for i in range(2, (int(math.sqrt(number)+1)) + 1):
        if number % i == 0:
            result = False
            break
    return result

def power_triple(limit):
    result = set()
    squares = [i for i in range(2, limit) if i**2 < limit and is_prime(i)]
    cubes = [i for i in range(2, limit) if i**3 < limit and is_prime(i)]
    fourths = [i for i in range(2, limit) if i**4 < limit and is_prime(i)]
    for i in fourths:
        for j in cubes:
            for k in squares:
                compute = k**2 + j**3 + i**4
                if compute < limit:
                    result.add(compute)
    result = sorted(result)
    print(f"There are {len(result)} numbers below {limit} that satisfy the condition")


def timer(func, *args):
    import time
    s = time.time_ns()
    func(args[0])
    e = time.time_ns()
    print(f"Took {(e-s)/10**9:.2f} seconds to compute.")

timer(power_triple, 50000000)

# There are 1097343 numbers below 50000000 that satisfy the condition
# Took 61.57 seconds to compute.
