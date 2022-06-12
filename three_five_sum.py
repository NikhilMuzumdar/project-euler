def three_five_sum(unto):
    sum = 0
    for n in range(1, unto):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    print(sum)
    return sum
