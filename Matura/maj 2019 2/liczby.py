lines = []
with open("przyklad.txt",encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

print(lines)

potegi = []
for i in range(11):
    potegi.append(3**i)

print(potegi)