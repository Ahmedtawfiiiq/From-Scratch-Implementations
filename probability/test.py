from random import randrange

x = 70
heads = tails = 0
for i in range(1000):
        if randrange(100) < x:
            heads = heads + 1
        else:
            tails = tails + 1

print(heads)
print(tails)
