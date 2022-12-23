# print("Hi")

class Human:
    imie = "Sebastian"

    def presentYourself(self):
        return "Hi my name is " + self.imie

obiekt = Human()
print(obiekt.imie)
print(obiekt.presentYourself())

obiekt2 = Human()
obiekt2.imie = "Adrian"
print(obiekt2.presentYourself())