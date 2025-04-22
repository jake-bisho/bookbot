from stats import count_words, char_freq, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book = get_book_text(filepath)
    word_count = count_words(book)
    freq_dict = char_freq(book)
    dict_list = sort_dict(freq_dict)

    # printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["num"]}")
    print("============= END ===============")

main()