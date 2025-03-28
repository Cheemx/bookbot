def count_words(text):
    num_words = text.split()
    return len(num_words)

def count_appearance_of_each_character(text):
    char_count = {}
    for c in text:
        c = c.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(char):
    return char["count"]

def sort_list_of_char_count(char_count):
    sorted_char_count = []
    for k, v in char_count.items():
        sorted_char_count.append({"char": k, "count": v})
        # print(k, v)
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count