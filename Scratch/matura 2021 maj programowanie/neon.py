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

        zmienna = 0
        while moj_napis[zmienna] != z[1]:
            zmienna += 1
        if ord(z[1])+1 > 90:
            nowa_liczba = chr(ord(z[1]) + 1 - 26)
        else:
            nowa_liczba = chr(ord(z[1])+1)



        moj_napis[zmienna] = nowa_liczba

wynik_koncowy = ""
for i in moj_napis:
    wynik_koncowy += i

dlugosc = len(wynik_koncowy)

#4.2
licznik = 1
save = 0
przewaga = ""
sam_poczatek_lista = []
for i in lines:
    rozdzielone = i.split()
    sam_poczatek_lista.append(rozdzielone[0])

for i in range(len(sam_poczatek_lista)-1):
    if sam_poczatek_lista[i] == sam_poczatek_lista[i+1]:
        # dwa takie same obok siebie
        licznik += 1
        if licznik > save:
            przewaga = sam_poczatek_lista[i]
            save = licznik

    else:
        # dwa różne obok siebie zatem zeruj
        licznik = 1

tablica = []
for i in lines:
    rozdzielone = i.split()
    if rozdzielone[0] == "DOPISZ":
        tablica.append(rozdzielone[1])

tablica.sort()
print(tablica)

the_most = 1
most_letter = ''
save = 1
for a in range(len(tablica)-1):
    if tablica[a] == tablica[a+1]:
        # poprzednie i nastepne są takie same
        the_most += 2
        if the_most > save:
            save = the_most
            most_letter = tablica[a]
    else:
        # poprzednie i następne są różne
        the_most = 0

print(most_letter)
print(save)

s = open('wynik4.txt', 'w')
s.write("4.1 " + str(dlugosc))
s.write("\n4.2 " + str(przewaga) + str(save))
# s.write("\n4.3 "+ )
s.write("\n4.4 " + str(wynik_koncowy))

# od 65 do 90