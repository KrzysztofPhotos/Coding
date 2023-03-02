plik = open("DANE/przyklad.txt.txt")
plik = plik.readlines()

zapis = open("4.1", "w")
ilosc_liczb = 0
x = 0
for line in plik:
    element = line.replace("\n", "")

    if element[0] == element[-1]:
        if x == 0:
            pierwszaliczba = element
            x = 1
        ilosc_liczb += 1

zapis.write(str(ilosc_liczb))
zapis.write(" " + str(pierwszaliczba))



################ 4.2 ###################
for line in plik:
    element = line.replace("\n", "")

