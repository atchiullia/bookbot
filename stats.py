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

def sort_chars(chars_dict):
    def sort_on(dict):
        return dict["num"]
    
    characters = [
        {"char": char, "num": count}
        for char, count in chars_dict.items()
        if char.isalpha()
    ]
    characters.sort(key=sort_on, reverse=True)
    return characters

