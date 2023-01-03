f = open("palindrome.txt", "r")

def palindrome(x):
    numLen = len(x) - 1
    #print(numLen)

    rest = numLen % 2
    if numLen % 2 == 1:
        # jesli liczba jest nieparzysta odejmij 1
        numLen -= 1

    print(numLen)

    numlen2 = numLen / 2

    n = 0
    for i in range(int(numlen2)):
        print(x[0])

count = 0
for line in f.readlines():
    count += 1

    palindrome(line)

    #print(line.strip())





