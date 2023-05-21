lines = []
with open('en_words.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

slowa = {}
for i in lines:
    if len(i) >= 19:
        slowa[i] = len(i)

print(slowa)