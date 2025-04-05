def get_book_text(file):
    file_contents = file.read()
    return file_contents

def main():
    # Open the file in read mode
    with open('books/frankenstein.txt', 'r') as file:
        # Read the content of the file
        text = get_book_text(file)
        print(text)    

main()
