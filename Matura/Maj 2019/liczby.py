lines = []
with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())


# print(lines)



potegi_3 = []
for i in range(100):
    number = 3 ** i
    potegi_3.append(number)
    # tablice już mamy z potegami 3

for i in range(99):
    if liczba == potegi_3[i]:
        print("jest jakas liczba")



wynik = 0
for num in lines:
    if czy_potega(num):
        wynik += 1

print(wynik)
