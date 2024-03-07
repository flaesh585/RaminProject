import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * math.pow(self.radius, 2)

try:
    r = int(input("Input the radius of a circle: "))
except ValueError:
    print("Incorrect input!")

circl1 = Circle(r)

print(circl1.radius)

print(circl1.area())