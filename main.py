import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sorted_chars = sort(char_count)
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("--------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for s in sorted_chars:
        chars = s["char"]
        nums = s["num"]
        if chars.isalpha():
            print(f"{chars}: {nums}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
