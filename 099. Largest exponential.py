import math
import time

s = time.time()


def log_value(number, power):
    return power * math.log(number)

max_sum = 0
line_count = 0
max_pair = [None]
with open("base_exponent.txt", mode="r") as file:
    for line in file.readlines():
        number = int(line.split(",")[0])
        power = int(line.split(",")[1])
        log = log_value(number, power)
        line_count += 1
        if log > max_sum:
            max_sum = log
            max_pair[0] = (number, power, line_count)

print(f"Answer: Number: {max_pair[0][0]} Exponent: {max_pair[0][1]} Line_No: {max_pair[0][2]}")
e = time.time()
print(f"Computed in {e - s:.2f} seconds.")
