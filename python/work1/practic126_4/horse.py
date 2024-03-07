class Horse():
    def __init__(self, c, name, owner):
        self.color = c
        self.name = name
        self.owner = owner
        print("Succescfully created!")

class Rider():
    def __init__(self, name):
        self.name = name

ramin = Rider("Ramin")
horse = Horse("black", "Ferrari", ramin)

print(horse.owner.name)