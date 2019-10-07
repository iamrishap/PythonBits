def word_break(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            # first condition checks that the word exists. Second checks that there is true at
            # the start of the word also (or the word is the first one itself)
            if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                d[i] = True
    print(d)
    return d[-1]


print(word_break('rishapisagoodrishapboyafterboyforall', ['is', 'for', 'boy', 'a', 'all', 'good', 'rishap', 'after']))
