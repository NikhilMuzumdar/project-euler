def digit_sum(number):
    dsum = 0
    number = str(number)
    for d in number:
        dsum += int(d)
    return dsum


max_sum = 0
for a in range(101):
    for b in range(101):
        s = digit_sum(a**b)
        if s > max_sum:
            max_sum = s
print(max_sum)
