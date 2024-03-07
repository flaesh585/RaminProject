import modulcube

try:
    number = int(input("Input a number: "))
except ValueError:
    print("Incorrect number!")

number = modulcube.cubed(number)

print(number)