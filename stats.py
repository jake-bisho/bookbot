def count_words(book):
    words = book.split()
    return len(words)

def char_freq(book):
    lowercase = book.lower()
    freq_dict = {}
    for c in lowercase:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    return freq_dict

def sort_dict(dict):
    dict_list = []
    for k in dict:
        new_dict = "character"


def sort_on(dict):
    return dict["num"]