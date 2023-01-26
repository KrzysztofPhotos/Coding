def isprime(num):
    if num < 2:
        return False
    i = 2
    while i <= num:
        if num % i == 0:
            return False
        return True

file = open("punkty.txt",   'r')
Lines = file.readlines()

obieliczbypierwsze = 0

count = 0
for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('r', '')

    x = tablica[0]
    y = tablica[1]

    if isprime(int(x)) and isprime(int(y)):
        obieliczbypierwsze += 1


print('obie liczby sa pierwsze: ' + str(obieliczbypierwsze))



