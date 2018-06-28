def longest(s):

    char_map = {}
    start = 0
    pos = 0
    longest = 0
    lstr = ""

    for index, char in enumerate(s):

        pos = char_map.get(char)
        if pos is not None and pos >= start:
            l = index - start
            if (index - start) > len(lstr):
                lstr = s[start:index]
            start = pos + 1
        char_map[char] = index

    if (len(s) - start) > len(lstr):
        lstr = s[start:]

    return lstr, len(lstr)

import sys

if __name__ == "__main__":
    print(longest("abcabcbb"))

