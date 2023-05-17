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

s = open("wynik4.txt","w")
s.write("4.1 " + str(ile))

