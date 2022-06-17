def divisor_sum(number):
    sum = 0
    for i in range(1, int((number/2)+1)):
        if number % i == 0:
            sum += i
    return sum

def both_ways(number):
    a = divisor_sum(number)
    if a == number:
        return False
    else:
        b = divisor_sum(a)
        return number == b

amicable = [i for i in range(10000) if both_ways(i)]
print(amicable)
print(sum(amicable))
