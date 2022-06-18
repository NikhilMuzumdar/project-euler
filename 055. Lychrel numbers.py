def is_palindrome(number):
    return str(number) == str(number)[::-1]

def mod_16(number):
    if number % 16 == 0:
        return "\n"
    else:
        return "\t"

def does_not_produces_palindromes(number):
    result = True
    number = int((str(number))) + int(str(number)[::-1])
    for i in range(50):
        if is_palindrome(number):
            result = False
            break
        else:
            number = int((str(number))) + int(str(number)[::-1])
    return result

def main(up_to):
    lychrel = [i for i in range(0, up_to+1) if does_not_produces_palindromes(i)]
    print(f"\nTotal numbers below 10,000 are: {len(lychrel)}")

main(10000)
