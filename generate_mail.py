from datetime import datetime
import sys

print("Mail generator")



type_of_service = input("Select which type of service did you do: \n1-> Refueling\n2 -> Cleaning\n3 -> Both")

if type_of_service == 1:
    service = "Refueling"
elif type_of_service == 2:
    service = "Cleaning"
elif type_of_service == 3:
    service = "Refueling and cleaning"

if type_of_service == 1:
    usluga = "Tankowanie"
elif type_of_service == 2:
    usluga = "Sprzątanie"
elif type_of_service == 3:
    usluga = "Tankowanie oraz sprzątanie"

# 1 refueling
# 2 cleaning
# 3 both

amount = input("Enter the amount: ")

bank_acc = input("\nSelect account do refund:\n1 -> MBank (my)\n2 -> Alior Bank\n3 -> Santander (my)\n4 -> Santander (Kuba)\n5 -> Revolut")

if bank_acc == 1:
    acc = "MBank"
    account_no = "89 1140 2004 0000 3102 7793 1648"
elif bank_acc == 2:
    acc = "Alior Bank"
    account_no = "56 2490 0005 0000 4000 0438 5955"
elif bank_acc == 3:
    acc = "Santander (my)"
    account_no = "55 1090 2053 0000 0001 5593 7297"
elif bank_acc == 4:
    acc = "Santander (Kuba)"
    account_no = "50 1090 2053 0000 0001 5603 1671"
elif bank_acc == 5:
    acc = "Revolut"
    account_no = "57 2910 0006 0000 0000 0440 0146"

date = input("Select day:\n1 -> Today\n2 -> Other day")

if date == 1:
    unformatted_date = datetime.now()
    date_input = unformatted_date.strftime('%d.%m.%Y')
elif date == 2:
    date_input = input("Enter a date in a format DD.MM.YY: ")

print("\nConfirm provided data: ")
print("Service: " + str(service))
print("Amount: " + str(amount) + " PLN")
print("Data: " + str(date_input))
print("Refund to account: " + str(acc))

confirm = input("Confirm that the data is okay: Y/N")
if confirm == "Y":
    write_mail()
else:
    sys.exit()

# confirmation at the end all date and Y/N






