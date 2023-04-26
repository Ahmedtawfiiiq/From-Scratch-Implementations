def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# move right or down
def gridTraveler(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)


def gridTraveler_memo(m, n, memo={}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    if (n, m) in memo:
        return memo[(n, m)]
    memo[(m, n)] = gridTraveler_memo(m - 1, n, memo) + gridTraveler_memo(m, n - 1, memo)
    return memo[(m, n)]


def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for number in numbers:
        difference = targetSum - number
        if canSum(difference, numbers) == True:
            return True  # stop early
    return False


# assume elements are all non-negative
# assume you can use an element as many times as needed
def canSum_memo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for number in numbers:
        difference = targetSum - number
        if canSum_memo(difference, numbers, memo) == True:
            memo[targetSum] = True
            return True  # stop early
    memo[targetSum] = False
    return memo[targetSum]


def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        difference = targetSum - number
        result = howSum(difference, numbers)
        if result is not None:
            result.append(number)
            return result  # stop early
    return None


def howSum_memo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        difference = targetSum - number
        result = howSum_memo(difference, numbers, memo)
        if result is not None:
            result.append(number)
            memo[targetSum] = result
            return result  # stop early
    memo[targetSum] = None
    return memo[targetSum]


def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest = []
    for number in numbers:
        difference = targetSum - number
        result = bestSum(difference, numbers)
        if result is not None:
            result.append(number)
            if len(shortest) == 0 or len(result) < len(shortest):
                shortest = result
            # return result  # stop early
    if len(shortest) == 0:
        return None
    return shortest


from copy import deepcopy


def bestSum_memo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return deepcopy(memo[targetSum])
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest = None
    for number in numbers:
        difference = targetSum - number
        result = bestSum_memo(difference, numbers)
        if result is not None:
            result.append(number)
            if shortest is None or len(result) < len(shortest):
                shortest = deepcopy(result)

    memo[targetSum] = shortest
    return deepcopy(memo[targetSum])


# write a function canConstruct(target, wordBank) that accepts a target string and an array of strings
# the function should return a boolean indicating
# whether or not the target can be constructed by concatenating elements of the wordBank array
# you may reuse elements of wordBank as many times as needed
def canConstruct(target, wordBank):
    if target == "":
        return True
    for ele in wordBank:
        if target.startswith(ele):
            result = target.replace(ele, "", 1)
            if canConstruct(result, wordBank):
                return True
    return False


def canConstruct_memo(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for ele in wordBank:
        if target.startswith(ele):
            result = target.replace(ele, "", 1)
            if canConstruct_memo(result, wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


def countConstruct(target, wordBank):
    if target == "":
        return 1
    count = 0
    for ele in wordBank:
        if target.startswith(ele):
            result = target.replace(ele, "", 1)
            count += countConstruct(result, wordBank)
    return count


def countConstruct_memo(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for ele in wordBank:
        if target.startswith(ele):
            result = target.replace(ele, "", 1)
            count += countConstruct_memo(result, wordBank, memo)
            memo[target] = count
    memo[target] = count
    return memo[target]


def allConstruct(target, wordBank):
    if target == "":
        return [[]]
    result = []
    for ele in wordBank:
        if target.startswith(ele):
            suffixWays = allConstruct(target.replace(ele, "", 1), wordBank)
            targetWays = [[ele] + way for way in suffixWays]
            result += targetWays
    return result


def allConstruct_memo(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for ele in wordBank:
        if target.startswith(ele):
            suffixWays = allConstruct_memo(target.replace(ele, "", 1), wordBank, memo)
            targetWays = [[ele] + way for way in suffixWays]
            result += targetWays
    memo[target] = result
    return memo[target]


# def allConstruct(target, wordBank):
#     if target == "":
#         return [[]]
#     result = []
#     for ele in wordBank:
#         if target.startswith(ele):
#             result = target.replace(ele, "", 1)
#             suffixWays = allConstruct(result, wordBank)
#             targetWays = [suffixWays]
#             targetWays += ele
#             result.append(targetWays)
#     return result


# print(canSum(7, [2, 3])) # true
# print(canSum(7, [5, 3, 4, 7])) # true
# print(canSum_memo(7, [2, 4]))  # false
# print(canSum(8, [2, 3, 5])) # true
print(canSum_memo(300, [7, 14]))  # false

# print(howSum_memo(7, [2, 3]))
# print(howSum_memo(7, [5, 3, 4, 7]))
# print(howSum_memo(7, [2, 4]))  # none
# print(howSum_memo(8, [2, 3, 5]))
# print(howSum_memo(300, [7, 14])) # none


# print(bestSum_memo(7, [5, 3, 4, 7]))
# print(bestSum_memo(8, [2, 3, 5]))
# print(bestSum_memo(8, [1, 4, 5]))
# print(bestSum_memo(100, [1, 2, 5, 25]))

# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
# print(
#     countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
# )  # false
# print(
#     allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# )  # true
# print(
#     allConstruct_memo(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee"]
#     )
# )  # true
# print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
