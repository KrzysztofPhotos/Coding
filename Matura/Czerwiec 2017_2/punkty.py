import sympy
import math

lines = []
with open('punkty.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())


def cyfropodobne(x, y):
    tablica_x = []
    tablica_y = []
    for i in range(len(str(x))):
        tablica_x.append(x[i])
    tablica_x.sort()
    tablica_x = list(dict.fromkeys(tablica_x))

    for i in range(len(str(y))):
        tablica_y.append(y[i])
    tablica_y.sort()
    tablica_y = list(dict.fromkeys(tablica_y))

    if tablica_x == tablica_y:
        return True
    else:
        return False
def policz_odleglosc(x1, y1, x2, y2):
    return round(math.sqrt((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2))
def polozenie_punktu(x, y):
    # srodek
    if int(x) < 5000 and int(y) < 5000:
        return "MID"
    elif int(x) > 5000 or int(y) > 5000:
        return "OUT"
    else:
        return "EDGE"


licznik = 0
licznik_cyfropodobne = 0
a = 0
b = 0
zewnatrz = 0
wewnatrz = 0
bok = 0
odleglosc = 0
for i in lines:
    rozdzielone = i.split(" ")

    # 4.1
    if sympy.isprime(int(rozdzielone[0])) and sympy.isprime(int(rozdzielone[1])):
        licznik += 1

    # 4.2
    if cyfropodobne(rozdzielone[0], rozdzielone[1]):
        licznik_cyfropodobne += 1

    # 4.3
    for punkt in lines:
        podgrupy = punkt.split(" ")
        if policz_odleglosc(rozdzielone[0], rozdzielone[1], podgrupy[0], podgrupy[1]) > odleglosc:
            a = podgrupy
            b = rozdzielone
            odleglosc = round(policz_odleglosc(rozdzielone[0], rozdzielone[1], podgrupy[0], podgrupy[1]))

    #4.4
    if polozenie_punktu(rozdzielone[0], rozdzielone[1]) == "OUT":
        zewnatrz += 1
    elif polozenie_punktu(rozdzielone[0], rozdzielone[1]) == "MID":
        wewnatrz += 1
    elif polozenie_punktu(rozdzielone[0], rozdzielone[1]) == "EDGE":
        bok += 1

s = open('wyniki4.txt','w')
s.write("4.1 " + str(licznik))
s.write("\n4.2 " + str(licznik_cyfropodobne))
s.write("\n4.3\nA:" + str(a) + "\nB: " + str(b) + "\nOdleglosc miedzy nimi: " + str(odleglosc))
s.write("\n4.4\n")
s.write("Krawedz: " + str(bok))
s.write("Wewnatrz: " + str(wewnatrz))
s.write("Zewnatrz: " + str(zewnatrz))
