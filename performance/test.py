import math


# M/M/m Queueing System
def p_0(rho, m):
    rho_hat = m * rho
    a = 1 / (1 - rho)
    b = math.pow(rho_hat, m) / math.factorial(m)
    c = 0
    for i in range(0, m):
        c += math.pow(rho_hat, i) / math.factorial(i)
    return 1 / ((a * b) + c)


def p_k(rho, m, k):
    rho_hat = m * rho
    p0 = p_0(rho, m)
    result = p0 * math.pow(rho_hat, k)
    if k <= m:
        result /= math.factorial(k)
    else:
        result /= math.factorial(m) * math.pow(m, k - m)
    return round(result, 3)


def erlang_c(rho, m):
    rho_hat = m * rho
    a = math.pow(rho_hat, m) / math.factorial(m)
    b = 0
    for i in range(0, m):
        b += math.pow(rho_hat, i) / math.factorial(i)
    b *= 1 - rho
    return round(a / (a + b), 3)


# def Tw(rho, m, Ts):
#     result = erlang_c(rho, m) * Ts / (m * (1 - rho))
#     return round(result, 3)


# def Tq(rho, m, Ts):
#     tw = Tw(rho, m, Ts)
#     return round(tw + Ts, 3)


#################################################################################
# M/M/infinity Queueing System


# def p_k(rho_hat, k):
#     return math.exp(-rho_hat) * math.pow(rho_hat, k) / math.factorial(k)


# def test(percentage, rho_hat):
#     k = 1
#     result = 0
#     while True:
#         result += p_k(rho_hat, k - 1)
#         if result >= percentage:
#             break
#         k += 1
#     return k


#################################################################################


# rho = 5 / 6
# m = 2
# ts = 1 / 6

# k = 2
# result = 0
# for i in range(0, k + 1):
#     result += p_k(rho, m, i)
# print(f"Probability of {k} or fewer customers in the system: {result}")

# print(p_k(rho, m, 2))

# print(erlang_c(0.8, 3))

# tq = Tq(rho, m, ts)
# print(f"Tq: {tq}")

# lq = m * rho * tq / ts
# print(f"Lq: {lq}")
#################################################################################

# percentage = 0.9
# rho_hat = 0.9
# m = test(percentage, rho_hat)
# rho = rho_hat / m
# ec = erlang_c(rho, m)

# print(f"m: {m}")
# print(f"rho: {rho}")
# print(f"Er: {ec}")

rho = 0.8 / 3
m = 3
print(f"erlang_c: {erlang_c(rho, m)}")
# print(f"p_0: {p_0(rho, m)}")
