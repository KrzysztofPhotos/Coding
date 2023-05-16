
mile = 0.621371192
kilometer = 1.609344

var = int(input("[Convert\n[Miles to kilometers -> matura 2021 czerwiec programowanie\n[Kilometers to miles -> 2\n"))
var2 = float(input("Type here a value to convert: "))

def mi_to_km():
    result = round(var2 * kilometer, 2)
    print(var2, "miles is equal to ", result, "kilometers.")

def km_to_mi():
    result = round(var2 * mile, 2)
    print(var2, " kilometers is equal to ",  result, "miles.")

if var == 1:
    # mi to km
    mi_to_km()
elif var == 2:
    # km to mi
    km_to_mi()
else:
    print("Bad value! matura 2021 czerwiec programowanie-2")

