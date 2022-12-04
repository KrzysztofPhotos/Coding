
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
    amount = float(input("Please type amount: "))
    product = product.strip()
    product = product.upper()
    shop_list[product] = amount
    print("Your product named", product, "was added to list.")

def show():
    print("\n[Your actual shopping list:")
    for i  in shop_list:
        print("[Product", i, "for price: $", shop_list[i])

def delete():
    to_del = input("Enter the name of the product you want to delete: ")
    to_del = to_del.upper()
    to_del = to_del.strip()
    if to_del in shop_list:
        shop_list.pop(to_del)
        print("Product named", to_del, "was delete.")
    else:
        print("You entered a bad name of product.\nTry again.")


while True:
    x = input("-> ")
    x = x.strip()
    x = x.upper()


    if str(x) == "+":
        # add a new element to dict
        add()
    elif str(x) == "-":
        # remove a element from dict
        delete()
    elif str(x) == "S":
        # show all shopping list
        show()
    elif str(x) == "F":
        # zakoncz liste zakupową
        add()
    elif str(x) == "HELP":
        help_request()
    else:
        print("Unknown command. Check the HELP")