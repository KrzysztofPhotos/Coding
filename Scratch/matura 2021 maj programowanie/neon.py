lines = []

with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())


moj_napis = []
for i in lines:

    z = i.split()
    if z[0] == "DOPISZ":
        moj_napis.append(str(z[1]))
    elif z[0] == "USUN":
        moj_napis.pop()
    elif z[0] == "ZMIEN":
        moj_napis.pop()
        moj_napis.append(str(z[1]))
    elif z[0] == "PRZESUN":



        zmienna = len(moj_napis)-1
        while moj_napis[zmienna] != z[1]:
            zmienna -= 1

        if ord(z[1])+1 > 90:
            nowa_liczba = chr(ord(z[1]) + 1 - 26)
        else:
            nowa_liczba = chr(ord(z[1])+1)



        moj_napis[zmienna] = nowa_liczba


print(moj_napis)

    # 65 - A
    # 90 - Z


