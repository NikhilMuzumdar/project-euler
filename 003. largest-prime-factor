# A Func to check if a number is prime and return True
def is_prime(number):
    result = True
    for i in range(2, (int(number / 2)) + 1):
        if number % i == 0:
            result = False
            break
    return result

# A function that returns the next prime number given a input number
def next_prime(input_number):
    next = input_number + 1
    while not is_prime(next):
        next += 1
    return next


def prime_factor(number):
    start = 2
    prime_factors = []
    remainder = number

    while remainder != 1:
        if remainder % start == 0:
            if start not in prime_factors:
                prime_factors.append(start)
            remainder = remainder / start
        else:
            start = next_prime(start)

    print(f"The prime factors of {number} are {prime_factors}\n{prime_factors[-1]} is the largest prime")


prime_factor(600851475143)
