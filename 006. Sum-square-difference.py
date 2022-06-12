def sum_of_squares(n):
  result = (n*(n+1)*(2*n + 1)) / 6
  return result

def square_of_sum(n):
  result = (n*(n + 1) / 2)**2
  return(result)

def find_diff(n):
  a = sum_of_squares(n)
  b  = square_of_sum(n)
  print(int(b-a))

find_diff(100)
