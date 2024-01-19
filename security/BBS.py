# blum blum shub
def check_pq(p, q):
    if p % 4 != 3 or q % 4 != 3:
        return False
    return True

def bbs(p, q, s):
    if not check_pq(p, q):
        print("p or q is not congruent to 3 mod 4")
        return None
    seq = []
    n = p * q
    x = (s * s) % n
    for i in range(10):
        x = (x * x) % n
        b = x % 2
        seq.append(b)
    return seq


p = 383
q = 503
s = 101355
seq = bbs(p, q, s)
print(seq)

