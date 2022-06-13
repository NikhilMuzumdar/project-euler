import time

def collatz_length(number):
  result = number
  count = 1 # Number itself is not tested in the while loop, hence we start at 1
  while result != 1:
    count += 1
    if number % 2 == 0:
      result = number / 2
    else:
      result = 3 * number + 1
    number = result
  return count

def first_longest_collatz(below):
  collatz_array = []
  length = 0
  for i in range(2, below):
    if collatz_length(i) > length:
      length = collatz_length(i)
      collatz_array.append((i, length))

  print(collatz_array[-1])


start = time.time()
first_longest_collatz(1000000)
end = time.time()
print(f"\nComputed in {end-start:.2f} sec")
