
lines = []
with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())


alfabet = ["A", "B","C",'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"]

wynik = []
for i in lines:
    print(i.split(" "))
    if i[0] == "DOPISZ":
        wynik.append(i[1])
    elif i[0] == "ZMIEN":
        wynik.pop()
        wynik.append(i[1])
    elif i[0] == "USUN":
        wynik.pop()
    elif i[0] == "PRZESUN":
        miejsce = alfabet.index(i[1]) # na którym miejscu jest dana litera
        wynik.pop()
        wynik.append(alfabet[int(miejsce)+1])

print(wynik)