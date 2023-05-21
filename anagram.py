def anagram(text1, text2):
    text1 = text1.upper()
    text2 = text2.upper()

    sum_text1 = 0
    sum_text2 = 0
    for i in text1:
        sum_text1 += ord(i)
    for i in text2:
        sum_text2 += ord(i)

    if sum_text1 == sum_text2:
        return True
    else:
        return False


txt = input("Type here first text: ")
txt2 = input("Type here second text: ")

print(anagram(txt, txt2))