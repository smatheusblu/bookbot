def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lowered_text = text.lower()
    counts = {}
    for char in lowered_text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [
        {"char": char, "num": count} for char, count in num_chars_dict.items()
    ]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
