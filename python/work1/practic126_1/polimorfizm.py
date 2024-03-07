class Rectangle:
    def __init__(self, a, b):
        self.side1 = a
        self.side2 = b
        print("Succesfuly Created!")
    
    def calculate_perimeter(self):
        return self.side1 + self.side2

class Square:
    def __init__(self, a):
        self.side1 = a
        print("Succesfuly Created!")

    def calculate_perimeter(self):
        return 4 * self.side1

rect = Rectangle(4, 9)
sqr = Square(5)

print("Perimeter of rectangle", rect.calculate_perimeter())
print("Perimeter of square", sqr.calculate_perimeter())