lines = []

with open('shopping_calculator.py', encoding="UTF-8") as f:
    for line in f:
        lines.append(line.strip())

print(lines)