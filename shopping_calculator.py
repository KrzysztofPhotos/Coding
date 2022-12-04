
# użytkownik wpisuje wartości
# na samym początku podajemy nasz budżet
# do wszystkiego jest funkcja (wartość, opis)
# na koniec wszystko jest sumowane oraz wypisana zostanie cała lista zakupowa wraz z ceną w ładnym wykonaniu

def help_request():
    print("\n[ <----- HELP ----->")
    print("[ Add a new item to shopping list -> +\n[ Delete a item from shopping list -> -\n[ Show all shopping list - S\n[ Complete the shopping list and save to the file -> F")

print("@-@-@   Welcome to shopping list calculator!   @-@-@\nIf you have any problems please try to solve problem by typing HELP")

while True:
    x = input("")
    x = x.strip()
    x = x.upper()


    if str(x) == "+":
        # dodaj nowy element do dict
    elif str(x) == "-":
        # usun element z listy
    elif str(x) == "S":
        # pokaż całą dotychczasową liste
    elif str(x) == "F":
        # zakoncz liste zakupową