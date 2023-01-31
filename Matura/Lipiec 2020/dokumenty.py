def palindrom(identyfikator):
    if identyfikator[2] == identyfikator[0]:
        return True
    elif identyfikator[3] == identyfikator[8] and identyfikator[4] == identyfikator[7] and identyfikator[5] == \
            identyfikator[6]:
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

#print(elementy)
#print(el_strip)

wyniki = open('wyniki4_2.txt', 'w')
for i in elementy:
    if palindrom(i):
        zmienna = str(i)
        wyniki.write(zmienna)
        wyniki.write("\n")

