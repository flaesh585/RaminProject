lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0

while True:
    print("Отгадай число от 1 до 9!")
    q = input()
    if q == "x":
        break
    print(lists[n])
    n = (n + 1) % 8