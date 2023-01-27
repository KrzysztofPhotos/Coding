file = open('Dane/mecz.txt')
file = file.read()

licznik_A = 0
licznik_B = 0
win = 0
licznik_wszystkich_pass = 0
najdluzsza_passa = 0
passa_druzyna = ''
for i in range(len(file)-1):
    if file[i] == file [i+1]:
        if file[i] == 'B':
            licznik_B += 1
            licznik_A = 0
            if licznik_B >= 10:
                licznik_wszystkich_pass += 1
                if licznik_B > najdluzsza_passa:
                    najdluzsza_passa = licznik_B
                    passa_druzyna = 'B'
        else:
            licznik_B = 0
            licznik_A += 1
            if licznik_A >= 10:
                licznik_wszystkich_pass += 1
                if licznik_A > najdluzsza_passa:
                    najdluzsza_passa = licznik_A
                    passa_druzyna = 'A'
    else:
        if file[i+1] == 'B':
            licznik_B = 1
        else:
            licznik_A = 1
        win += 1

#print(passa_druzyna)
#print(najdluzsza_passa)
print(licznik_wszystkich_pass)

f = open('wyniki1.txt', 'w')
f.write('1.1\n' + str(win) + '\n')
f.write('1.3\nNajdluzsza dobra passe o dlugosci ' + str(najdluzsza_passa) + ' osiagnela druzyna ' + str(passa_druzyna))
f.close()


