def get_book_text(file):
    file_contents = file.read()

    return file_contents

def number_of_words(text):
    words = text.split()
    num_words = len(words)

    return num_words

def main():
    with open('books/frankenstein.txt', 'r') as file:
        text = get_book_text(file)
        num_words = number_of_words(text)
        print(f'{num_words} words found in the document')

main()
