import math

def is_prime(number):
    result = True
    for i in range(2, (int(math.sqrt(number)+1)) + 1):
        if number % i == 0:
            result = False
            break
    return result

def prime_sum(upto):
    prime_array = [element for element in range(2, upto) if element %2 != 0 and is_prime(element)]
    print(sum(prime_array)+2)

prime_sum(2000000)
