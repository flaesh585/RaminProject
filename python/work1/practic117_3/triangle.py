class Triangle:
    def __init__(self, a, h):
        self.side = a
        self.height = h
    
    def area(self):
        return (self.side * self.height) / 2

try:
    a = int(input("Input a side of a triangle: "))
    h = int(input("Input a height to this side of triangle: "))
except ValueError:
    print("Incorrect input!")

trin1 = Triangle(a, h)

print("Side: ", trin1.side)
print("Height: ", trin1.height)
print("Area: ", trin1.area())