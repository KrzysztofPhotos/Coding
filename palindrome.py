import math


def palindrome(text):
    for i in range(math.floor(len(text)/2)):
        if not text[i] == text[-1-int(i)]:
            return False
        return True


x = input("Enter text to check: ")

if palindrome(x):
    print("It is palindrome")
else:
    print("It is not palidrome")
