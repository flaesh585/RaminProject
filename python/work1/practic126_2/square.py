class Square:
    def __init__(self, a):
        self.side = a
        print("Succesful created!")

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, x):
        self.side = self.side + x

sqr = Square(5)
print("length of a side: ", sqr.side)

try:
    num = int(input("Input a number: "))
except ValueError:
    print("Incorrect Input!")

sqr.change_size(num)

print(sqr.side)