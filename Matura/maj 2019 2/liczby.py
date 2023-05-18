import math

lines = []
with open("liczby.txt",encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

potegi = []
for i in range(11):
    potegi.append(3**i)

h = 0
for i in lines:
    # patrzymy na jedna linijek
    for n in range(11):
        if int(i) == int(potegi[n]):
            h += 1

s = open("wyniki4.txt",'w')
s.write("4.1 " + str(h))

# 4.2
takie = []
# rozbijam liczbe na pojedyncze cyfry
for i in lines:
    wynik = 0
    for znak in i:
        wynik += math.factorial(int(znak))
    if int(i) == int(wynik):
        takie.append(i)

s.write("\n\n4.2")
for i in takie:
    s.write(str(i) + "\n")


