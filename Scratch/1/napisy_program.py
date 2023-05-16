
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

with open("przyklad.txt", encoding='UTF-8') as f:
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

