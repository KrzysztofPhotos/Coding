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



