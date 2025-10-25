def count_num_words(text):
    count = text.split()
    return len(count)


def get_num_characters(text):
    text = text.lower()
    counter = {}
    for char in text:
        if (char in counter):
            counter[char] += 1
        else:
            counter[char] = 1
    return counter
        