# return a dict of words
file_path = '/Users/cyborg/Documents/VsCode/TestGit/project-euler/098A. p098_words.txt'
def read_data(file_name):
    from collections import OrderedDict
    with open(file_name, mode='r') as file:
        words = file.readlines()[0].replace('"', "") .split(',')

    word_map = {}
    for word in words:
        if len(word) in word_map:
            word_map[len(word)].append(word)
        else:
            word_map[len(word)] = [word]

    word_map = OrderedDict(sorted(word_map.items()))
    return word_map

def filter_anagram_list(word_list):
    array = []
    for i, value in enumerate(word_list):
        t = i+1
        while t < len(word_list):
            if ''.join(sorted(value)) == ''.join(sorted(word_list[t])):
                array.extend([value, word_list[t]])
            t += 1
    return array

def filter_anagram_dict(word_map):
    zero_len_index = []
    for key in word_map:
        word_map[key] = filter_anagram_list(word_map[key])
        if len(word_map[key]) == 0:
            zero_len_index.append(key)

    for key in zero_len_index:
        word_map.pop(key)

    return word_map


def main():
    word_map = read_data(file_path)
    anagram_word_dict = filter_anagram_dict(word_map)
    for key in anagram_word_dict:
        print(key, anagram_word_dict[key])

main()
