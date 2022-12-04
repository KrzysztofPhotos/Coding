

# the program asks user to 3 numbers and the program has to organise from smallest to highest

print("Hello to program called find the largest among the numbers\nYour task will be type three VARIOUS numbers!\n")


a = float(input("Type first value: "))
b = float(input("Type second value: "))
c = float(input("Type third value: "))

if a > b > c:
    print(a,">",b, ">", c)
elif a > c > b:
    print(a, ">", c, ">", b)
elif b > a > c:
    print(b, ">", a, ">", c)
elif b > c > a:
    print(b, ">", c, ">", a)
elif c > a > b:
    print(c, ">", a, ">", b)
elif c > b > a:
    print(c, ">", b, ">", a)
elif a == b == c:
    print(a, "==", b, "==", c)
else:
    print('Error.')