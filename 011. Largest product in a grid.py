import numpy as np
import math
import time

start = time.time()
array = []
with open("string.txt", mode="r") as file:
    for lines in file.readlines():
        array.append([int(element) for element in lines.split("\n")[0].split(" ")])

high_sum = 0
np_array = np.array(array)


def max_sum(np_array):
    np_array = np_array[:4, :4]
    product_array = []
    # Row max
    for rows in np_array[:4]:
        product_array.append(math.prod(rows))
    # Col Max
    for columns in np_array.transpose():
        product_array.append(math.prod(columns))
    # Diagonal
    product_array.append(math.prod(np_array.diagonal()))
    product_array.append(math.prod(np_array[::-1].diagonal()))

    return max(product_array)



for i in range(20-4):
    for j in range(20-4):
        if max_sum(np_array[i:i+4, j:j+4]) > high_sum:
            high_sum = max_sum(np_array[i:i+4, j:j+4])

print(high_sum)

end = time.time()

print(f"Took {end-start:.2f} seconds")
