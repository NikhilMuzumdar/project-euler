import string

text = ""
with open("string.txt", mode="r") as file:
    for line in file.readlines():
        text += line[:-1] # Do not include \n

def max_product(n_consecutive):
    i = 0
    product = 1
    result = 0
    for i in range(0, len(text)-n_consecutive):
        selected_string = text[i:i+n_consecutive]
        for l in selected_string:
            product *= int(l)
        if product > result:
            result = product
        product = 1

    print(result)

max_product(13)
