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