def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def num_value(my_dict):
    value = my_dict["num"]
    return value


def sort(char_count):
    sorted = []
    for char in char_count:
        count = char_count[char]
        my_dict = {"char": char, "num": count}
        sorted.append(my_dict)
    sorted.sort(key=num_value, reverse=True)
    return sorted
