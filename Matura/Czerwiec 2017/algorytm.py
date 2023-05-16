def isprime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def usunduplikaty(tab):
    tab.sort()
    i = 0
    dlugosc = len(tab)
    while i < dlugosc - 1:
        if tab[i] == tab[i + 1]:
            tab.pop(i)
            dlugosc = - 1
        else:
            i += 1
    return tab


def porownaj(tab1, tab2):
    if len(tab1) == len(tab2):
        for ie in range(len(tab1)):
            if tab1[ie] != tab2[ie]:
                return False
        return True
    else:
        return False

# def najdalszy():
#     Lines2 = Lines.copy()
#     for sline in range(len(Lines)):
#         Lines[sline] = Lines[sline].replace('\n', '')
#         x = Lines[sline[0]]
#
#         for sline2 in range(len(Lines)):
#
#
#         print(Lines[sline])
        #for el in range(len(Lines)):
        #    print(Lines[el])


file = open("punkty.txt", 'r')
Lines = file.readlines()

obieliczbypierwsze = 0
krawedz = 0
wewnatrz = 0
zewnatrz = 0
similarnum = 0
count = 0

for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('r', '')
    x = tablica[0]
    y = tablica[1]

    # 4.matura 2021 czerwiec programowanie
    if isprime(int(x)) and isprime(int(y)):
        obieliczbypierwsze += 1

    # 4.2
    lista_x = []
    for i in x:
        lista_x.append(i)
    lista_x.sort()

    lista_y = []
    for i in y:
        lista_y.append(i)
    lista_y.sort()

    if porownaj(usunduplikaty(lista_x), usunduplikaty(lista_y)):
        similarnum += 1

    # 4.3

    # 4.4
    if int(x) == -5000 or int(x) == 5000 and -5000 <= int(y) <= 5000:
        krawedz += 1
    elif int(y) == -5000 or int(y) == 5000 and -5000 <= int(x) <= 5000:
        krawedz += 1
    elif 5000 > int(x) > -5000 and 5000 > int(y) > -5000:
        wewnatrz += 1
    else:
        zewnatrz += 1

print('obie liczby sa pierwsze: ' + str(obieliczbypierwsze))
print('na zewnatrz ' + str(zewnatrz))
print('wewnatrz: ' + str(wewnatrz))
print('krawedz: ' + str(krawedz))

print("\r cyfropodobne: " + str(similarnum))

#najdalszy()