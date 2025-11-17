from stats import get_num_words, get_chars_dict, get_sorted_list
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")

    for item in get_sorted_list(chars_dict):
        print(f"{item['char']}: {item['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
