
def czy_palindrom(tekst):
    lewo = 0
    prawo = len(tekst)-1

    while lewo < prawo:
        if tekst[lewo] == tekst[prawo]:
            lewo += 1
            prawo -= 1
        else:
            return False
    return True

lines = []

with open("napisy.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

numerki = 0
for i in lines:
    for k in range(len(i)):
        if i[k].isnumeric():
            numerki += 1

s = open("wynik4.txt", "w")
s.write("4.1 " + str(numerki) + "\n")


odp = ""
zmienna_liczba = 19
cyferka = 0
for i in range(50):
    aktualne = lines[zmienna_liczba]
    znaczek = aktualne[cyferka]
    odp += str(znaczek)
    zmienna_liczba += 20
    cyferka += 1

s.write("\n4.2 " + str(odp) + "\n")

napis = ""
for i in lines:
    na_poczatku = i[49] + str(i)
    na_koncu = str(i) + i[0]
    if czy_palindrom(na_poczatku):
        napis += na_poczatku[25]
    if czy_palindrom(na_koncu):
        napis += na_koncu[25]

s.write("\n4.3 " + str(napis) + "\n")


haslo = ""
for i in lines:
    # jesteśmy w 1 wierszu (linijce)
    liczba = ""
    for k in i:
        if k.isnumeric():
            liczba += str(k)
    if len(liczba) % 2 == 0:
        print("")
    else:
        liczba = liczba[:-1]

    haslo += str(liczba)
    # if int(liczba) % 2 == 1:
    #     print(liczba)
    #     liczba = str(liczba[:-1])
    # print(liczba)
print(len(haslo))


i = 0
for i in range(int(len(haslo)/2)):
    numper = haslo[i] + haslo[i+1]

    i += 2

    if 65 <= int(numper) <= 90:
        # spelnia warunki
        # print("wieksza od 65 lub mniejsza od 90")
        # print(numper)

