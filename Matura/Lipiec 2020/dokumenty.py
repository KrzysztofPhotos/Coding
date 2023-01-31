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
    wartosci = {"A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15,
                "G": 16,
                "H": 17,
                "I": 18,
                "J": 19,
                "K": 20,
                "L": 21,
                "M": 22,
                "N": 23,
                "O": 24,
                "P": 25,
                "Q": 26,
                "R": 27,
                "S": 28,
                "T": 29,
                "U": 30,
                "V": 31,
                "W": 32,
                "X": 33,
                "Y": 34,
                "Z": 35
                }
    if identyfikator[0]


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


wyniki = open('wyniki4_2.txt', 'w')
for i in elementy:
    if palindrom(i):
        zmienna = str(i)
        wyniki.write(zmienna)
        wyniki.write("\n")

