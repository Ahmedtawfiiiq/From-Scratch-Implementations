# function to check if a number is power of 2 or not
def powerOfTwo(x):
    # return (x and (not(x & (x - 1))))
    r1 = x & (x - 1)
    print(r1)
    r2 = not (
        r1
    )  # if r1 > 0 then r2 = False else r2 = True (r2 only True if x is power of 2)
    print(r2)
    r3 = x and r2  # to check if x is zero then return False
    print(r3)
    return r3


print(powerOfTwo(3))
