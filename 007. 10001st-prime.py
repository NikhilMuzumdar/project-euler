import time
def is_prime(number):
    result = True
    for i in range(2, (int(number / 2)) + 1):
        if number % i == 0:
            result = False
            break
    return result


# A function that returns the next prime number given a input number
def next_prime(input_number):
    next = input_number + 1
    while not is_prime(next):
        next += 1
    return next

def nth_prime(n):
  array = [2]
  count = 1
  while count != n:
    array.append(next_prime(array[-1]))
    count += 1

  print(f"The {n}th prime is {array[-1]}")

# To measure time taken 
start = time.time()
nth_prime(10001)
end = time.time()
print(f"Took {(end-start):.2f} seconds")
