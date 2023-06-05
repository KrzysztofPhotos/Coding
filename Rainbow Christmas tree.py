import random
from colorama import Fore, init

init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]

for i in range(30):
    treeText = " " * (29 - i)
    treeText += "".join([random.choice(colors) + ("#" if j % 2 == 0 else " ") for j in range(i * 2 + 1)])
    print(treeText)
for i in range(3):
    print(" " * 27 + f"{'# '.join([random.choice(colors) for _ in range(3)])}#")