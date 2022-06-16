import math
import time
start_time = time.time()


def is_prime(number):
    if number == 1:
      return False
    if number == 2:
      return True
    result = True
    for i in range(2, (int(math.sqrt(number)+1)) + 1):
        if number % i == 0:
            result = False
            break
    return result

# check if all digits are prime
def next_prime(input_number):
    next = input_number + 1
    while not is_prime(next):
        next += 1
    return next


def truncable_prime(number):
  result = True
  number = str(number)
  for i in range(0, len(number)):
    # print(f"Left: {number[0:i+1]} Right: {number[-(i+1):]}")
    if is_prime(int(number[0:i+1])) and is_prime(int(number[-(i+1):])):
      continue
    else:
      result = False
      break
  return result

tp_array = []
start = 10
while len(tp_array) != 11:
  if truncable_prime(start):
    tp_array.append(start)
    # print(tp_array)
    start = next_prime(start)
  else:
    start = next_prime(start)

print(f"The sum is {sum(tp_array)}")

end_time = time.time()
print(f"Took {end_time-start_time:.2f} seconds")
