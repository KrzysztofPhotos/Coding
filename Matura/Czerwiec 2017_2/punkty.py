import sympy
lines = []
with open('punkty.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())




licznik = 0
for i in lines:
    rozdzielone = i.split(" ")
    if sympy.isprime(int(rozdzielone[0])) and sympy.isprime(int(rozdzielone[1])):
        licznik += 1


s = open('wyniki4.txt','w')
s.write("4.1 " + str(licznik))
