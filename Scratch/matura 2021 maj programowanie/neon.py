lines = []

with open("instrukcje.txt", encoding='UTF-8') as f:
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

        zmienna = 0

        while moj_napis[zmienna] != z[1]:
            zmienna += 1
            print(zmienna)
        if ord(z[1])+1 > 90:
            nowa_liczba = chr(ord(z[1]) + 1 - 26)
        else:
            nowa_liczba = chr(ord(z[1])+1)



        moj_napis[zmienna] = nowa_liczba

wynik_koncowy = ""
for i in moj_napis:
    wynik_koncowy += i

s = open('wynik4.txt','w')
# s.write("4.1 "+ )
# s.write("\n4.2 "+ )
# s.write("\n4.3 "+ )
s.write("\n4.4 " + str(wynik_koncowy))