
mile = 0.621371192
kilometer = 1.609344

var = int(input("[Convert\n[Miles to kilometers -> 1\n[Kilometers to miles -> 2\n"))
var2 = float(input("Type here a value to convert: "))

def mi_to_km():
    print(var2 * kilometer)


def km_to_mi():
    print(var2 * mile)

if var == 1:
    # mi to km
    mi_to_km()
elif var == 2:
    # km to mi
    km_to_mi()
else:
    print("Bad value! 1-2")

