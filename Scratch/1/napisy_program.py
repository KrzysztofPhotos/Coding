
lines = []

with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())
    #print(lines)


numerki = ""
for i in lines:
    for k in range(len(i)):
        if i[k].isnumeric():
            numerki += str(i[k])

dlugosc = len(numerki)
s = open("wynik4.txt", "w")
s.write("4.1 " + str(dlugosc) + "\n")


odp = ""
zmienna_liczba = 19
cyferka = 0
for i in range(50):
    aktualne = lines[zmienna_liczba]
    znaczek = aktualne[cyferka]
    odp += str(znaczek)
    zmienna_liczba += 20
    cyferka += 1

s.write("\n4.2 " + str(odp))
