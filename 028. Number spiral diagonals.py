
# More of a math problem 
# proof here: https://www.educative.io/answers/how-to-solve-the-number-spiral-diagonals-problem

def dig_sum(dim):
    n = (dim - 1) / 2
    sums = (3 + 2 * n * (8 * n ** 2 + 15 * n +13)) / 3
    print(int(sums))

dig_sum(1001)
