# monte carlo simulation to estimate the area of a circle
# using random numbers

import random
import math


def circle_area(r):
    return math.pi * r**2


def square_area(l):
    return l**2


def circle_fn(r, x1, y1):
    # generate random numbers between zero and one
    x = -4 + (2 * r * random.random())
    y = -3 + (2 * r * random.random())
    return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)


def estimate_area_circle(r, x1, y1, n=1000000):
    m = 0
    for _ in range(n):
        if circle_fn(r, x1, y1) <= r:
            m += 1
    return (m / n) * square_area(2 * r)


estimate = estimate_area_circle(r=5, x1=1, y1=2)
real = circle_area(5)
print(f"Estimated Area: {estimate}")
print(f"Real Area: {real}")
print(f"Error: {abs(estimate - real)}")
