def get_num_words(text):
    list = text.split()
    return len(list)


def get_char_counts(text):
    counts = {}
    for char in text:
        lowered_char = char.lower()
        counts[lowered_char] = counts.get(lowered_char, 0) + 1
    return counts


def sort_on(item):
    return item["num"]


def sort_char_counts(char_counts_dict):
    sorted_list = []
    for char, count in char_counts_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
