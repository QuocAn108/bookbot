from stats import get_num_words, get_char_counts
BOOK_PATH = "books/frankenstein.txt"


def get_book_text(path):
    try:
        with open(path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy file tại đường dẫn {path}"
    except Exception as e:
        return f"Đã xảy ra lỗi khi đọc file: {e}"


def main():
    book_text = get_book_text(BOOK_PATH)
    print(book_text)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(book_text)
    print(char_counts)


if __name__ == "__main__":
    main()
