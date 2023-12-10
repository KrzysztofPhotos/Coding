class Complex:
    def __init__(self, realpart, imagpart): 
        self.r = realpart
        self.i = imagpart
    def conjugate(self):
        self.i = -self.i
        
x = Complex(2.0, -1.0)
a = x.r # 2.0
b = x.i # -1.0
x.conjugate()
print(x.i) # 1.0


