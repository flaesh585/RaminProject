class Apple:
    def __init__(self, c, t, w, j):
        self.color = c
        self.taste = t
        self.weight = w
        self.juicy = j
        print("Создано!")

object1 = Apple("Зелёный", "Сладкий", 56, True)
print(object1)
print("Какого цвета яблоко? ", object1.color)
