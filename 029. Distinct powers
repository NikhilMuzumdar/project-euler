import math
import time


def main(upper, lower):
    from itertools import product
    a = list(range(lower, upper + 1))
    b = set()
    for l in product(a, repeat=2):
        b.add(l[0] ** l[1])
    b = sorted(b)
    print(len(b))
    return 0

def main1(upper, lower):
    from itertools import product
    a = list(range(lower, upper + 1))
    b = set()
    for l in product(a, repeat=2):
        b.add(math.pow(l[0], l[1]))
    b = sorted(b)
    print(len(b))
    return 0

def timer(func, *args):
    s = time.time_ns()
    func(args[1], args[0])
    e = time.time_ns()
    print(f"Took {(e-s)/1000:.2f} micro-seconds to compute.")



timer(main, 2, 100)
timer(main1, 2, 100)
