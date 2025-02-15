print("digite:")
a = float(input())

print("digite:")
b = float(input())

print("digite:")
c = float(input())

delta = b ** 2 - 4 * a * c
print(delta)

import math
x1 = (-b + math.sqrt(delta)) / 2 * a
x2 = (-b - math.sqrt(delta)) / 2 * a

print(x1)
print(x2)