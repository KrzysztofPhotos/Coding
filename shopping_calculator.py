
# użytkownik wpisuje wartości
# na samym początku podajemy nasz budżet
# do wszystkiego jest funkcja (wartość, opis)
# na koniec wszystko jest sumowane oraz wypisana zostanie cała lista zakupowa wraz z ceną w ładnym wykonaniu

def help_request():
    print("\n[ <----- HELP ----->")
    print("[ Add a new item to shopping list -> +\n[ Delete a item from shopping list -> -\n[ Show all shopping list - S\n[ Complete the shopping list and save to the file -> F")

print("@-@-@   Welcome to shopping list calculator!   @-@-@\nIf you have any problems please try to solve problem by typing HELP")

#define a empty dict

shop_list = dict()

def add():
    product = str(input("Please type a name of the product / service: "))
    amount = float(input("Please type amount"))
    shop_list[product] = amount
    print("Your product named", product, "was added to list.")




while True:
    x = input("-> ")
    x = x.strip()
    x = x.upper()


    if str(x) == "+":
        # add a new element to dict
        add()
    elif str(x) == "-":
        # remove a element from dict
        add()
    elif str(x) == "S":
        # show all shopping list
        add()
    elif str(x) == "F":
        # zakoncz liste zakupową
        add()
    elif str(x) == "HELP":
        help_request()
    else:
        print("Unknown command. Check the HELP")