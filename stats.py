def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    char_count_dict = {}

    lowercase_contents = text.lower()
    individual_chars = list(lowercase_contents)

    for char in individual_chars:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1

    return char_count_dict

def sort_on(items):
    return items["count"]

def get_sorted_dict_list(dict):
    dict_list = []

    for key, value in dict.items():
        dict_list.append({"char": key, "count": value})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
