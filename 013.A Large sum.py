import string
num_string = ""
digit_array = []
with open("string.txt", mode="r") as file:
  for line in file.readlines():
    digit_array.append(line)
digit_array = [int(element.split("\n")[0]) for element in digit_array]
print(str(sum(digit_array))[:10])

#  The last line does not have a \n, hence returns error if you only read lines up to [:-1]
