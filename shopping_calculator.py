import sys
from datetime import datetime

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
    if len(shop_list) == 0:
        print("\n[ Your actual shopping list is blank.")
    else:
        print("\n[ Your actual shopping list:")
        for i  in shop_list:
            print("[ Product", i, "for price: $", shop_list[i])

def delete():
    to_del = input("Enter the name of the product you want to delete: ")
    to_del = to_del.upper()
    to_del = to_del.strip()
    if to_del in shop_list:
        shop_list.pop(to_del)
        print("Product named", to_del, "was delete.")
    else:
        print("You entered a bad name of product.\nTry again.")

def finish():
    ask = input("Are you sure to save and exit the shopping list? Y/N ")
    ask = ask.strip()
    ask = ask.upper()
    if str(ask) == "Y":
        print("\n[ Your final shopping list:")
        final_price = 0
        for i in shop_list:
            print("[ Product", i, "for price: $", shop_list[i])
            final_price = final_price + float(shop_list[i])

        len_dic = len(shop_list)

        print("[\n[ Summary:\n[ Products ->",len_dic,"\n[ Final amount:", final_price)

        to_file = input("\nDo you want to save list as file? Y/N")
        to_file = to_file.strip()
        to_file = to_file.upper()
        if str(to_file) == "Y":
            now = datetime.now()
            name_of_the_file = "results " + str(now) + str(".txt")
            print(name_of_the_file) # tymczasowe
            f = open(str(name_of_the_file),"x")
            f.write("Hello there")
            f.close()
        else:
            sys.exit("End of program without saving results")

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
        # finish and save the shopping list
        finish()
    elif str(x) == "HELP":
        help_request()
    else:
        print("Unknown command. Check the HELP")