# print("Hi")

class Human:
    def __init__(self):

    imie = "Sebastian"

    def presentYourself(self, powitanie = "Hi"):
        return powitanie + " my name is " + self.imie

obiekt = Human()
print(obiekt.imie)
print(obiekt.presentYourself("Witam"))

obiekt2 = Human()
obiekt2.imie = "Adrian"
print(obiekt2.presentYourself())