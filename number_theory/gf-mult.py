# galois fields mulitplication
# m(x) = x^8 + x^4 + x^3 + x + 1

# f(x) = x6 + x4 + x2 + x + 1
# g(x) = x7 +x + 1

# find f(x) * g(x) mod m(x)
#  (01010111) * (10000011) mod (100011011)


def gf_2_8_multplication(f, g):
    m = 0b00011011
    # x * f(x) = f(x) << 1 if f(x) < 128 else (f(x) << 1) ^ m
    # from x to x^7 assume ord(f(x)) < 8 and ord(g(x)) < 8
    # create array of 8 bytes
    results = [0] * 8
    for i in range(8):
        if i == 0:
            results[i] = f & 0xff
        else:
            results[i] = (results[i - 1] << 1) & 0xff
            if results[i - 1] >= 128:
                results[i] ^= m
            results[i] &= 0xff
    # read g(x) from right to left
    # if g(x) == 1 then xor with f(x)
    result = 0
    for i in range(8):
        if g & 1:
            result ^= results[i]
        g >>= 1
    # return only last 8 bits
    return result


f = 0b01010111
g = 0b10000011
result = gf_2_8_multplication(f, g)
print(bin(result))
