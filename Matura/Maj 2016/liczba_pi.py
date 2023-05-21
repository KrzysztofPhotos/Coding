from math import *

lines = []
with open('punkty.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

#print(lines[0].split(" "))

r = 100
for punkt in lines:
    #print(punkt)
    pkt = punkt.split(" ")
    x = pkt[0]
    y = pkt[1]
    if sqrt(((int(x) - 200)**2) + ((int(y) - 200) ** 2)) == r:
        print("nalezy")

# kwadrat o boku 200
# środek symetrii 200;200


print(-200**2)