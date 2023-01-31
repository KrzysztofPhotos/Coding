def palindrom(identyfikator):
    if identyfikator[2] == identyfikator[0]:
        return True
    elif identyfikator[3] == identyfikator[8] and identyfikator[4] == identyfikator[7] and identyfikator[5] == \
            identyfikator[6]:
        return True
    else:
        return False


def kontrola(identyfikator):
    rezultat = 0
    wartosci = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
                "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
                "W": 32, "X": 33, "Y": 34, "Z": 35}
    var_1 = identyfikator[0]
    var_2 = identyfikator[1]
    var_3 = identyfikator[2]
    var_1 = wartosci[var_1]
    var_2 = wartosci[var_2]
    var_3 = wartosci[var_3]
    rezultat += int(var_1) * 7 + int(var_2) * 3 + int(var_3) + int(identyfikator[4]) * 7 + int(identyfikator[5]) * 3 + int(identyfikator[6]) + int(identyfikator[7]) * 7 + int(identyfikator[8]) * 3

    liczbadodzielenia = identyfikator[3]

    if rezultat % 10 == liczbadodzielenia:
        return True
    else:
        return False


plik = open("DANE/identyfikator.txt")
plik = plik.readlines()

suma = []
elementy = []
el_strip = []
for line in plik:
    element = line.replace("\n", "")
    striped = element.strip("QWERTYUIOPASDFGHJKLZXCVBNM")
    elementy.append(element)
    el_strip.append(striped)

wyniki2 = open('wyniki4_2.txt', 'w')
for i in elementy:
    if palindrom(i):
        zmienna = str(i)
        wyniki2.write(zmienna)
        wyniki2.write("\n")

wyniki3 = open('wyniki4_3.txt', 'w')
for i in elementy:
    print(i)
    if kontrola(i):
        zmienna = str(i)
        wyniki3.write(zmienna)
        wyniki3.write("\n")