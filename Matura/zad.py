import numpy

file = open("punkty.txt", 'r')
Lines = file.readlines()

count = 0
zawiera = 0
for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('\r', '')

    x = tablica[0]
    y = tablica[1]


    if -5000 <= int(x) <= 5000 and -5000 <= int(y) <= 5000:
        zawiera = zawiera + 1


print(zawiera)



