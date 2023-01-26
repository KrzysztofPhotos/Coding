file = open("Czerwiec 2017/punkty.txt", 'r')
Lines = file.readlines()

def isprime(number):
    if number < 2:
        return False
    i = 2
    while i <= number:
        if number % i == 0:
            return False
        return True

# def cyfropodobne(x, y):


count = 0
srodek = 0
zewnatrz = 0
krawedz = 0
obapierwsze = 0

for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('\r', '')

    x = tablica[0]
    y = tablica[1]

    # krawędzie góra i dół
    if int(y) == 5000 or int(y) == -5000 and -5000 <= int(x) <= 5000:
        krawedz += 1

    # krawędzie prawo i lewo
    elif int(x) == 5000 or int(x) == -5000 and -5000 <= int(y) <= 5000:
        krawedz += 1

    # środek
    elif -5000 < int(x) < 5000 and -5000 < int(y) < 5000:
        srodek += 1

    # zewnątrz
    else:
        zewnatrz += 1

    if isprime(int(x)) and isprime(int(y)):
        obapierwsze += 1


f = open('wynik4.txt', 'w')
f.write('4.1\nObie wspolrzedne sa liczbami pierwszymi: ' + str(obapierwsze))
f.write("\n\n4.4")
f.write("\nNa krawedziach: " + str(krawedz))
f.write("\nPoza kwadratem: " + str(zewnatrz))
f.write("\nW srodku kwadratu: " + str(srodek))
f.close()