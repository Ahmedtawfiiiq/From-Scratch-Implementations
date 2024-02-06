# what is the base case ?
# what is the smallest amount of work i can do in each iteration ?


def reverseString(s):
    # base cases
    # there is only one character in the string
    if len(s) == 0:
        return ""

    return reverseString(s[1:]) + s[0]


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
    return s[0] == s[-1] and isPalindrome2(
        s[1:-1]
    )  # shrink the string for the next call


# ispalindrome iterative
def isPalindrome3(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


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


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x * x, n // 2)
    return x * power(x, n - 1)


# print(sumNaturalNumbers(50))
# print(isPalindrome2("racecar"))
# print(getSequences([1, 2, 3], 0))
print(power(1e-5, 100000))
