def kmp_search(haystack, needle): # Knuth–Morris–Pratt algorithm
    word = needle
    string = haystack
    i = 0  # current character position of word
    j = 0  # current character position of string

    if not word:
        return 0
    while j < len(string):
        if word[i] == string[j]:
            i += 1
            j += 1
            if i == len(word):
                return j - i  # only first matched need to be return
        else:
            i = get_kmp_table_index(i, word)
            if i == 0:
                i += 1
                j += 1
    return -1

def get_kmp_table_index(i, word):
