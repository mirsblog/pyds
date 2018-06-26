import sys

def longestSubString(s):

    if not s:
        return ""

    start = 0
    end = 0
    longest = ""

    found = []
    while end < len(s):
        c = s[end]
        end += 1

        # char is unique
        if c not in found:
            found.append(c)
            if end - start > len(longest):
                longest = s[start:end]
            continue

        # char repeats
        # move start forward
        while start < end -1:
            if s[start] != c:
                start += 1
                found.pop(0)
            else:
                start+=1
                break

    return longest


if __name__ == "__main__":
    s = longestSubString(sys.argv[1])
    print(s, len(s))
