from stats import count_num_words, get_num_characters, get_a_sorted_list_of_dicts
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def print_report(file_path, num_of_words, list_of_sorted_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for dict in list_of_sorted_dicts:
        if (dict['char'].isalpha()):
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


                

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        content = get_book_text(file_path)
        number_of_words = count_num_words(content)
        char_counter = get_num_characters(content)
        list_of_sorted_dicts = get_a_sorted_list_of_dicts(char_counter)
        print_report(file_path, number_of_words, list_of_sorted_dicts)

main()

