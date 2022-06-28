def read_word():
    """Reads the word from file and returns a list"""
    with open("coordinates.txt", mode="r") as file:
        word_list = file.read().split(",")

    word_list = [element.replace('"', "") for element in word_list]
    return word_list

def word_value(word):
    """Takes word as a string and returns it's value (Ex: a = 1, z = 26).
    Cases are ignored! """
    from string import ascii_lowercase
    word_sum = 0
    word_dict = dict(zip(ascii_lowercase, list(range(1,27))))
    for l in word.lower():
        word_sum += word_dict[l]
    return word_sum

def traingle_numbers(up_to):
    """Generates triangle numbers up to a limit"""
    triangle_numbers = [1]
    i = 2
    while triangle_numbers[-1] < up_to:
        triangle_numbers.append(int(i * (i + 1) * 0.5))
        i += 1
    return triangle_numbers

def main():
    triangle_words = 0
    triangle_number_list = traingle_numbers(200)
    word_list = read_word()
    for word in word_list:
        if word_value(word) in triangle_number_list:
            triangle_words += 1

    print(f"Triangle word in the file is: {triangle_words}")

if __name__ == '__main__':
    main()
