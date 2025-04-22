from stats import count_words, char_freq

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = count_words(book)
    freq_dict = char_freq(book)
    print(f"{word_count} words found in the document")
    print(freq_dict)

main()