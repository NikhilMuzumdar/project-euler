def even_fib_sum(upto):
    fib = [1, 2]
    even_sum = 0
    while fib[-1] < upto:
        last = sum(fib[-2:])
        if last < upto:
            fib.append(last)
        else:
            break
    even = [element for element in fib if element % 2 == 0]
    even_sum = sum(even)
    print(even_sum)
