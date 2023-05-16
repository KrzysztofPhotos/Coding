f = open("palindrome.txt", "r")

def palindrome(x):
    numLen = len(x) - 1

    rest = numLen % 2
    if numLen % 2 == 1:
        # jesli liczba jest nieparzysta odejmij matura 2021 czerwiec programowanie
        numLen -= 1

    numlen2 = numLen / 2

    n = 0
    last = len(x)
    for i in range(int(numlen2)):
        print(x[n])
        print(x[int(last)])
        print(" ")

count = 0
for line in f.readlines():
    count += 1

    palindrome(line)

    #print(line.strip())





