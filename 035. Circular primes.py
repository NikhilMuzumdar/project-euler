def is_prime(number):
    import math
    if number == 1:
        return False
    if number == 2:
        return True
    result = True
    for i in range(2, (int(math.sqrt(number) + 1)) + 1):
        if number % i == 0:
            result = False
            break
    return result


def rotate_number(number=197):
    number = str(number)
    circular_numbers = []

    if len(number) == 1:
        circular_numbers.append(int(number))
    else:
        for _ in range(len(number)):
            number = number[1::] + number[0]
            circular_numbers.append(int(number))
    return circular_numbers


def all_prime(a_list):
    """Given a list, checks if all numbers in the list are primes"""
    for num in a_list:
        if not is_prime(num):
            return False
    return True


def timer(func, *args):
    """Timer function to check the execution time"""
    import time
    s = time.time_ns()
    func(args[0])
    e = time.time_ns()
    print(f"Took {(e - s) / 10 ** 9:.2f} seconds to compute.")


def main(up_to):
    count = 0
    for i in range(1, up_to + 1):
        rotations = rotate_number(i)
        if all_prime(rotations):
            count += 1
    print(count)


timer(main, 1000000)
