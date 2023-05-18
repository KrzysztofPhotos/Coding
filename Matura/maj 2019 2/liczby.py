lines = []
with open("przyklad.txt",encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

print(lines)

potegi = []
for i in range(11):
    potegi.append(3**i)

print(potegi)

h = 0
for i in lines:
    # patrzymy na jedna linijek
    for n in range(11):
        if int(i) == int(potegi[n]):
            h += 1

s = open("wyniki4.txt",'w')
s.write("4.1 " + str(h))



