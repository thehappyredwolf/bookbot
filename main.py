def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def count_num_words(text):
    count = text.split()
    return len(count)

def main():
    file_path = "books/frankenstein.txt"
    content = get_book_text(file_path)
    number_of_words = count_num_words(content)
    print(f"Found {number_of_words} total words")

main()

