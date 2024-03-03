from datetime import datetime
import sys
import pyperclip

def write_mail(usluga, kwota, data, konto):
    tekst = f"""
    Dzień dobry,

    Piszę w sprawie ostatniego zlecenia z programu Ogarniam ({usluga}). Niestety, byłem zmuszony skorzystać z własnej karty płatniczej, ponieważ nie było karty flotowej dostępnej w pojeździe.

    W załączniku znajduje się faktura VAT za transakcję, która została wzięta na firmę Traficar. Numery rejestracyjne znajdują się na fakturze.

    Proszę o zwrot poniesionych kosztów na numer konta: {konto} 
    Kwota: {kwota} PLN
    Data: {data}

    Będę wdzięczny za potwierdzenie otrzymania tej wiadomości oraz informację o procesie zwrotu środków.

    Dziękuję i pozdrawiam.

    Z poważaniem,
    Krzysztof Kwiatkowski
    """
    pyperclip.copy(tekst)
    return tekst

print("Mail generator")

services = {1: "Tankowanie", 2: "Sprzątanie", 3: "Tankowanie oraz sprzątanie"}
accounts = {
    1: ("MBank", "89 1140 2004 0000 3102 7793 1648"),
    2: ("Alior Bank", "56 2490 0005 0000 4000 0438 5955"),
    3: ("Santander (my)", "55 1090 2053 0000 0001 5593 7297"),
    4: ("Santander (Kuba)", "50 1090 2053 0000 0001 5603 1671"),
    5: ("Revolut", "57 2910 0006 0000 0000 0440 0146")
}

type_of_service = int(input("Select which type of service did you do:\n1 -> Refueling\n2 -> Cleaning\n3 -> Both\n"))
usluga = services.get(type_of_service, "Nieokreślona usługa")

amount = input("\nEnter the amount: ")

bank_acc = int(input("\nSelect account do refund:\n1 -> MBank (my)\n2 -> Alior Bank\n3 -> Santander (my)\n4 -> Santander (Kuba)\n5 -> Revolut\n"))
acc, account_no = accounts.get(bank_acc, ("Nieokreślone konto", "Nieokreślony numer"))

date_selection = int(input("\nSelect day:\n1 -> Today\n2 -> Other day\n"))
date_input = datetime.now().strftime('%d.%m.%Y') if date_selection == 1 else input("Enter a date in a format DD.MM.YY: ")

print("\nConfirm provided data: ")
print(f"Service: {usluga}")
print(f"Amount: {amount} PLN")
print(f"Data: {date_input}")
print(f"Refund to account: {acc}")

confirm = input("\nConfirm that the data is okay: Y/N ")
if confirm.lower() == "y":
    print(write_mail(usluga, amount, date_input, account_no))
else:
    print("Operation stopped")
    sys.exit()
