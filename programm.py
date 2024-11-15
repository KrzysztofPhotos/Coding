import math

a = 12
b = 6

limit = (a + b) ** 3

print(a)
print(b)

while True:
    c = a + b
    if c > limit:
        break
    print(c)
    a = b
    b = c
