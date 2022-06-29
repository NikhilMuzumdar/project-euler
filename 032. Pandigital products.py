

def is_pan_digital(num1, num2):
    product = num1 * num2
    (num1, num2, product) = (str(num1), str(num2), str(product))
    joined_string = num1+num2+product
    joined_string = sorted([int(i) for i in joined_string])
    return joined_string == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_all_pandigital():
    pan_dict = {}
    # In total we have 9 digit nums, only two combinations that can result in a 9 digit number
    # 1-digit number times a 4-digit number as well as a 2-digit number times a 3-digit number.
    # below case covers both
    dig_2 = [i for i in range(1, 99)]
    dig_3 = [i for i in range(1, 9999)]
    for m in dig_2:
        for n in dig_3:
            if is_pan_digital(m, n):
                pan_dict[m*n] = (m, n)
    print(pan_dict)
    print(sum(pan_dict.keys()))

find_all_pandigital()
