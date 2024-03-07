class Square():
    def __init__(self, a):
        self.side = a
        self.out = "{} on {} on {} on {}".format(self.side, self.side, self.side, self.side)
        print("Succesful created!")

    def __repr__(self):
        print(self.out)

    def calculate_perimeter(self):
        return 4 * self.side

    def __str__(self):
        return str(self.out)

sqr = Square(5)

print(sqr)