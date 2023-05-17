lines = []
with open('sygnaly.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

x = 39
slogan = ''
for i in range(25):
    linia = lines[x]
    x += 40
    slogan += linia[9]

s = open("wynik4.txt",'w')
s.write("4.1 " + slogan)

# 4.2
literki_max = 0
linijka = ""
for i in lines:
    literki_licz = 0
    for n in range(26):
        if i.count(chr(int(65 + n))) > 0:
            # dana literka sie zawiera w linijce
            literki_licz += 1

    if literki_licz > literki_max:
        literki_max = literki_licz
        linijka = i

s.write("\n\n4.2 " + linijka + " " + str(literki_max))

# 4.3


def sprawdzaj(slowo):
    # mamy slowo (linijke)
    for i in range(len(slowo)):
        # przechodzimy tyle razy jak dlugi jest wyraz
        for j in range(len(slowo)):
            if abs(ord(slowo[i]) - ord(slowo[j])) > 10:
                return False
    return True


s.write("\n\n4.3\n")
for x in lines:
    if sprawdzaj(x):
        s.write("\n" + x)
