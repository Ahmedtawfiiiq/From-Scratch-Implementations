# time complexity: O(n)
# space complexity: O(n)
def tab_fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i + 1 < n:
            table[i + 2] += table[i]
    return table[n]


# time complexity: O(n)
# space complexity: O(n)
def bottomUp_fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def tab_grid(m, n):
    table = np.zeros((m + 1, n + 1), dtype=int)
    table[1][1] = 1
    # for i in range(1, m + 1):
    #     table[i][1] = 1
    # for j in range(1, n + 1):
    #     table[1][j] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if i + 1 <= m:
                table[i + 1][j] += current
            if j + 1 <= n:
                table[i][j + 1] += current
    # print(table)
    return table[m][n]


import numpy as np


def bottomUp_grid(m, n):
    table = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        table[i][1] = 1
    for j in range(1, n + 1):
        table[1][j] = 1
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m][n]


def tab_canSum(target, numbers):
    table = np.zeros((target + 1), dtype=bool)
    table[0] = True
    for i in range(target + 1):
        if table[i] == True:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = True
    # print(table)
    return table[target]


def tab_howSum(target, numbers):
    table = np.empty((target + 1), dtype=object)
    table[0] = []
    for i in range(target + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = [ele for ele in table[i]]  # O(m) m is target size
                    table[i + num].append(num)
    return table[target]


def tab_bestSum(target, numbers):
    table = np.empty((target + 1), dtype=object)
    table[0] = []
    for i in range(target + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    shortest = [ele for ele in table[i]]
                    shortest.append(num)
                    if table[i + num] is None or len(shortest) < len(table[i + num]):
                        table[i + num] = [ele for ele in shortest]
    return table[target]


def tab_canConstruct(target, wordBank):
    table = np.zeros((len(target) + 1), dtype=bool)
    table[0] = True
    for i in range(len(target)):
        if table[i] == True:
            for word in wordBank:
                if word == target[i : i + len(word)]:
                    table[i + len(word)] = True
    # print(table)
    return table[len(target)]


def tab_countConstruct(target, wordBank):
    table = np.zeros((len(target) + 1), dtype=int)
    table[0] = 1
    for i in range(len(target) + 1):
        if table[i] != 0:
            for word in wordBank:
                if word == target[i : i + len(word)]:
                    table[i + len(word)] += table[i]
    # print(table)
    return table[len(target)]


def tab_allConstruct(target, wordBank):
    table = np.empty((len(target) + 1), dtype=object).tolist()
    table[0] = [[]]
    for i in range(len(target) + 1):
        if table[i] is not None:
            for word in wordBank:
                if word == target[i : i + len(word)]:
                    if table[i + len(word)] is None:
                        table[i + len(word)] = []
                    for ele in table[i]:
                        table[i + len(word)].append([e for e in ele] + [word])
    # print(table)
    return table[len(target)]


# print(tab_howSum(7, [2, 3]))
# print(tab_howSum(7, [5, 3, 4, 7]))
# print(tab_howSum(7, [2, 4]))
# print(tab_howSum(8, [2, 3, 5]))
# print(tab_howSum(300, [7, 14]))

# print(tab_bestSum(7, [5, 3, 4, 7]))
# print(tab_bestSum(8, [2, 3, 5]))
# print(tab_bestSum(8, [1, 4, 5]))
# print(tab_bestSum(100, [1, 2, 5, 25]))

print(tab_allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # true
# print(
#     tab_countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
# )  # false
# print(
#     tab_countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# )  # true
# print(
#     tab_countConstruct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee"]
#     )
# )  # true
# print(tab_allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
