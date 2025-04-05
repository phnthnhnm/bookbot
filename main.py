from stats import get_num_words

def get_book_text(file):
    file_contents = file.read()

    return file_contents

def main():
    with open('books/frankenstein.txt', 'r') as file:
        text = get_book_text(file)
        num_words = get_num_words(text)
        print(f'{num_words} words found in the document')

main()
