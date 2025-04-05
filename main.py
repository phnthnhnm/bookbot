import sys
from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(file):
    file_contents = file.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")

    with open(sys.argv[1], 'r') as file:
        print("Analyzing book found at " + sys.argv[1] + "...")

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
