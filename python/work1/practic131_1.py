class Square():
    all_objects = []

    def __init__(self, a):
        self.side = a
        self.all_objects.append(self.side)
        print("Succesfully completed!")

    def __repr__(self):
        return str(self.side)

sqr1 = Square(12)
sqr2 = Square(5)
sqr3 = Square(7)

print(sqr1)

print("All: ", Square.all_objects)