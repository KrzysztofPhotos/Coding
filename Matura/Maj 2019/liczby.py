import math
lines = []
with open("liczby.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

ile = 0
for liczba in lines:
    for i in range(11):
        z = 3**i
        if int(liczba) == int(z):
            ile += 1

s = open("wynik4.txt", "w")
s.write("4.1 " + str(ile) + "\n\n")

s.write("4.2")
for element in lines:
    # rozbijamy na kawałki
    temp = []
    for cyfra in element:
        temp.append(cyfra)
    #print(temp)
    wynik = 0
    for k in temp:
        wynik += math.factorial(int(k))
    #print(wynik)
    if int(element) == int(wynik):
        s.write("\n" + str(element))
