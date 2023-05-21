lines = []
with open('en_words.txt', encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

slowa = {}
for i in lines:
    if len(i) >= 19:
        slowa[i] = len(i)

print(slowa)

# numerami = {}
#
# for slowo in lines:
#     if len(slowo) >= 19:
#         numerami[len(slowo)] = slowo
#
# print(numerami)

tabelka = ['he', 'puu']
slowniczek = {}

slowniczek['xD'] = tabelka

print(slowniczek)

oceny = [2,4,5,2,5,2,3,4,2]

for i in range(len(oceny)):
    print(oceny[i], end=" ")

for ocena in oceny:
    print(ocena, end=" ")

for i, ocena in enumerate(oceny):
    print(i, ocena)