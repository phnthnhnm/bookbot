from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(file):
    file_contents = file.read()

    return file_contents

def main():
    print("============ BOOKBOT ============")
    with open('books/frankenstein.txt', 'r') as file:
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        text = get_book_text(file)
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        char_count = get_char_count(text)
        sorted_list = get_sorted_list(char_count)
        for item in sorted_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['count']}")
        print("============= END ===============")

main()
