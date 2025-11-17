def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]


def get_sorted_list(char_dict):
    result = []
    for ch, count in char_dict.items():
        if ch.isalpha():
            result.append({"char": ch, "num": count})
    result.sort(key=sort_on, reverse=True)
    return result
