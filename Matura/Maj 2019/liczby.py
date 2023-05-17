lines = []
with open("liczby.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

print(lines)