# what is the base case ?
# what is the smallest amount of work i can do in each iteration ?


def reverseString(s):
    # base cases
    # there is only one character in the string
    if len(s) == 0:
        return ""

    return reverseString(s[1:]) + s[0]


def decimalToBinary(num):
    if num == 0:
        return ""
    return decimalToBinary(num // 2) + str(num % 2)


def sumNaturalNumbers(num):
    if num == 0:
        return 0
    return sumNaturalNumbers(num - 1) + num


def isPalindrome(s):
    # base case
    # there is only one character or no characters in the string
    if len(s) == 0 or len(s) == 1:
        return True
    # recursive condition
    elif s[0] == s[-1]:
        # shrink the string for the next call
        return isPalindrome(s[1:-1])
    # base case
    # when first and last elements of the string are different
    else:
        return False


print(sumNaturalNumbers(50))
