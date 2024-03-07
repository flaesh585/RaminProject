class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
        print("Succesfully created!")

    def what_am_i(self):
        print("i'm a shape")

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rct = Rectangle(4, 8)
sqr = Square(5, 5)

print(sqr.what_am_i())
print("Perimeter of rectangle equal to: ", rct.calculate_perimeter())
print("Perimeter of square equal to: ", sqr.calculate_perimeter())