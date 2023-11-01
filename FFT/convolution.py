# a and b are of 3rd degree
a_coef = [0, 0, 0, 6, 7, -10, 9][::-1]  # pad till size of c
b_coef = [0, 0, 0, -2, 0, 4, -5][::-1]  # pad till size of c
c_coef = []

j = 0
k = 0
while j <= 6:  # c is of 6th degree
    c = 0
    while k <= j:
        c += a_coef[k] * b_coef[j - k]
        k += 1
    c_coef.append(c)
    j += 1
    k = 0
c_coef = c_coef[::-1]
print(c_coef)
