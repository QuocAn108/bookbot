def get_num_words(text):
    list = text.split()
    return len(list)


def get_char_counts(text):
    counts = {}
    for char in text:
        lowered_char = char.lower()
        counts[lowered_char] = counts.get(lowered_char, 0) + 1
    return counts
