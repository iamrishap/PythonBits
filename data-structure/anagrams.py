from collections import defaultdict

# def load_words(filename='/usr/share/dict/american-english'):
#     with open(filename) as f:
#         for word in f:
#             yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.items():
        if len(anagrams) > 1:
            print(key, anagrams)

# word_source = load_words()
# print_anagrams(word_source)

word_source = ["car", "tree", "boy", "girl", "arc", "bone", "nobe", "oneb"]
print_anagrams(word_source)