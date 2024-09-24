# longest prefix suffix
def LPS(pattern):
    m = len(pattern)
    lps = [0] * m
    l = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[l]:
            lps[i] = l + 1
            l += 1
            i += 1
        elif l == 0:
            lps[i] = 0
            i += 1
        else:
            l = lps[l - 1]
    return lps


def kmp(text, pattern):
    lps = LPS(pattern)
    n = len(text)
    m = len(pattern)
    j = 0
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == m:
            return i - m
    return -1


text = "ABABDABACDABABCABAB"
pattern = "AAACAAAA"
print(LPS(pattern))
print(kmp(text, pattern))
