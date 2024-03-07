class Shape():
    def __init__(self, l, w):
        self.width = w
        self.length = l
        print("Succesfully Created!")

class Reactangle(Shape):
    pass

class Square(Reactangle):
    pass

fiqura = Shape(7, 3)
priyam = Reactangle(10, 5)
kvadrat = Square(5, 5)

same_kvadrat = kvadrat

print(same_kvadrat is kvadrat)
print(priyam is fiqura)
print(kvadrat is fiqura)
print(kvadrat is priyam)