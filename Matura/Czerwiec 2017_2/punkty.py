import sympy
lines = []
with open('punkty.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

def cyfropodobne(x,y):
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


cyfropodobne("22113377","32172")

licznik = 0
licznik_cyfropodobne = 0
for i in lines:
    rozdzielone = i.split(" ")
    if sympy.isprime(int(rozdzielone[0])) and sympy.isprime(int(rozdzielone[1])):
        licznik += 1

    if cyfropodobne(rozdzielone[0],rozdzielone[1]):
        licznik_cyfropodobne += 1

s = open('wyniki4.txt','w')
s.write("4.1 " + str(licznik))
s.write("\n4.2 " + str(licznik_cyfropodobne))