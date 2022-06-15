def is_palindrome(number):
    return str(number) == str(number)[::-1]

def db_palindrome(number):
    base_10 = number
    base_2 = bin(number)[2:]
    return is_palindrome(base_2) and is_palindrome(base_10)

def sum_palindrome(under):
    pal_array = []
    for number in range(1, under):
        if db_palindrome(number):
            pal_array.append(number)

    p = sum(pal_array)
    print(p)
    return p

sum_palindrome(1000000)
