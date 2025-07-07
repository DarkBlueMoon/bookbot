from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_dict_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")

    num_chars = get_num_characters(text)
    # print(num_chars)

    sorted_char_list = get_sorted_dict_list(num_chars)
    # print(report)

    get_report(book_path, num_words, sorted_char_list)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_report(filepath, num, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            char = item["char"]
            count = item["count"]
            print(f"{char}: {count}")

    print("============= END ===============")

main()