file = open("punkty.txt", 'r')
Lines = file.readlines()

count = 0
srodek = 0
zewnatrz = 0
krawedz = 0

for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('\r', '')

    x = tablica[0]
    y = tablica[1]

    # krawędzie góra i dół
    if int(y) == 5000 or int(y) == -5000 and -5000 <= int(x) <= 5000:
        krawedz += 1

    # krawędzie prawo i lewo
    elif int(x) == 5000 or int(x) == -5000 and -5000 <= int(y) <= 5000:
        krawedz += 1

    # środek
    elif -5000 < int(x) < 5000 and -5000 < int(y) < 5000:
        srodek += 1

    # zewnątrz
    else:
        zewnatrz += 1


print(srodek)
print(krawedz)
print(zewnatrz)


f = open('wynik4.txt', 'w')
f.write("Na krawedziach: " + str(krawedz))
f.write("\nPoza kwadratem: " + str(zewnatrz))
f.write("\nW srodku kwadratu: " + str(srodek))
f.close()