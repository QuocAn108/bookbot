import sys
from stats import get_num_words, get_char_counts, sort_char_counts


def get_book_text(path):
    try:
        with open(path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        return f"Error: File not found at {path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    if "Error:" in book_text:
        print(book_text)
        sys.exit(1) 
    num_words = get_num_words(book_text)
    char_counts_dict = get_char_counts(book_text)
    sorted_char_list = sort_char_counts(char_counts_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
