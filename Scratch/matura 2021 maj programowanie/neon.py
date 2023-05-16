lines = []

with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())


moj_napis = ""
for i in lines:

    z = i.split()
    print(z[0])
    if z[0] == "DOPISZ":
        print('dopisz')
    elif z[0] == "USUN":
        print('kasuj to')
    elif z[0] == "ZMIEN":
        print("zmieniaj mi to")
    elif z[0] == "PRZESUN":
        print("przesuwaj to mi!")