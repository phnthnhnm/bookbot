def get_num_words(text):
    words = text.split()
    num_words = len(words)

    return num_words

def get_char_count(text):
    dict = {}

    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
            
    return dict
