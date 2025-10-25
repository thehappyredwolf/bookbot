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
        

def sort_on(items):
    return items["num"]

def get_a_sorted_list_of_dicts(dictionary):
    list = []
    for item in dictionary:
        list.append({"char": item, "num": dictionary[item]})
    list.sort(reverse=True, key=sort_on)
    return list