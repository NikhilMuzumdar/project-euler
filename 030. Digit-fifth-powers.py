# Finding the upper bound is the secret to solving this problem. The rest is straight forward.
# Determine the upper bound. We need to find a number x 9^5 which gives us an x digit number.
# We can do this by hand. Since 95 = 59049, we need at least 5 digits. 5*9^5 = 295245,
# so with 5 digits we can make a 6 digit number. 6*9^5 = 354294.
# So 355000 seems like a reasonable upper bound to use.
# We could probably tighten is even further if we wanted.

limit = 6 * 9**5
def fifth_pow_digit(number):
  sum = 0
  temp = str(number)
  for d in temp:
    sum += int(d)**5
  return sum

five = [element for element in range(2, limit) if element == fifth_pow_digit(element)]
print(five)
print(sum(five))
