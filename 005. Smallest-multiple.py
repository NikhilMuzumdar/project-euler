# Smallest number divisible through 1 to 20:

# Start from 2520 which is divisible 1 through 10
# increment 20 and check whether all divide

def all_through_20(number):
  divisible = True
  for i in range(20, 10, -1):
  # Check from 20 to 11, rest will divide any ways
    if number % i != 0:
      divisible = False
      break
  return divisible

def find_all_through_20():
  number = 2520
  while not all_through_20(number):
    number += 20

  print(number)

find_all_through_20()
    
