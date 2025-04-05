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

def sort_on_count(dict):
    return dict["count"]

def get_sorted_list(char_count):
    sorted_list = []
    
    for char, count in char_count.items():
        sorted_list.append({'char': char, 'count': count})

    sorted_list.sort(key=sort_on_count, reverse=True)

    return sorted_list
