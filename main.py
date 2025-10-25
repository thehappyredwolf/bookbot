def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    file_path = "books/frankenstein.txt"
    content = get_book_text(file_path)
    print(content)

main()

