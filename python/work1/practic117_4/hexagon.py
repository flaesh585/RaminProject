class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.first = a
        self.second = b
        self.third = c
        self.fourth = d
        self.fifth = e
        self.sixth = f
        print("Successfully created!")

    def calculate_perimeter(self):
        return a + b + c + d + e + f

try:
    a, b, c = int(input("Input the first side: ")), int(input("Input the second side: ")), int(input("Input the third side: "))
    d, e, f = int(input("Input the fourth side: ")), int(input("Input the fifth side: ")), int(input("Input the sixth side: "))
except ValueError:
    print("Incorrect input!")

hex1 = Hexagon(a, b, c, d, e, f)

print(hex1.calculate_perimeter())