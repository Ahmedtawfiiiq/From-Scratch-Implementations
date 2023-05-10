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


def isPalindrome2(s):
    # base case
    # there is only one character or no characters in the string
    if len(s) <= 1:
        return True
    # recursive condition
    return s[0] == s[-1] and isPalindrome(
        s[1:-1]
    )  # shrink the string for the next call


def getSequences(arr, i):
    # base case
    if i == len(arr):
        return [[]]
    # recursive case
    sequences = getSequences(arr, i + 1)
    result = []
    for seq in sequences:
        result.append(seq)
        result.append([arr[i]] + seq)
    return result


print(sumNaturalNumbers(50))
print(isPalindrome2("racecar"))
print(getSequences([1, 2, 3], 0))
