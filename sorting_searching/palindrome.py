def isPalindrome(s):
    # base case
    # there is only one character or no characters in the string
    if len(s) <= 1:
        return True
    # recursive condition
    return s[0] == s[-1] and isPalindrome(
        s[1:-1]
    )  # shrink the string for the next call


print(isPalindrome("racecar"))
