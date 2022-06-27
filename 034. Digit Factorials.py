# Trick is to find the upper limit, explaination here: https://www.xarg.org/puzzle/project-euler/problem-34/
import math

def dig_fac_sum(number):
    number = str(number)
    fac_sum = 0
    for l in number:
        fac_sum += math.factorial(int(l))
    return fac_sum

fac_9 = math.factorial(9)

digi_factorials = [(i, dig_fac_sum(i)) for i in range(3, int(fac_9 * 7)) if i == dig_fac_sum(i)]

d_sum = 0
for _ in digi_factorials:
    d_sum += _[0]

print(f"The Digit factorial sum is {d_sum}")


# The Digit factorial sum is 40730
