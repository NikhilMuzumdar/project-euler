# The largest number that is a product of two 3 digit numbers and is a palindrome

# Create an array of product of all 3 digit numbers
def palindrome_three_dig_product():
  number = 0
  for i in range(999, 100-1, -1):
    for j in range(999, 100-1, -1):
      p = i*j
      string_p = str(p)
      if string_p == string_p[::-1] and p > number:
        number = p
  print(number)

palindrome_three_dig_product()
