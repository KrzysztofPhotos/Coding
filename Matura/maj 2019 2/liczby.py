import math

lines = []
with open("liczby.txt", encoding='UTF-8') as f:
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

s = open("wyniki4.txt", 'w')
s.write("4.1\n" + str(h))

# 4.2
takie = []
# rozbijam liczbe na pojedyncze cyfry
for i in lines:
    wynik = 0
    for znak in i:
        wynik += math.factorial(int(znak))
    if int(i) == int(wynik):
        takie.append(i)

s.write("\n\n4.2 \n")
for i in takie:
    s.write(str(i) + "\n")

# 4,3

for i in range(len(lines)-1):

    dwa = math.gcd(int(lines[i]), int(lines[i+1]))
    x = math.gcd(dwa, int(lines[i+2]))
    if x > 1:
        if math.gcd(x, int(lines[i+3])) > 1:

    else:
        # od nowa liczyć trzeba zacząć

