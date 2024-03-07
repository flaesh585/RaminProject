def five(x, y, z, d=10, e=9):
    return (x + y + z) * d + e

print("Function for x, y, z and optionaly d, e")
print("Input basic or all(with optionaly)")
action = input()

if action == "basic":
    print("Input x, y, z")
    X = int(input())
    Y = int(input())
    Z = int(input())
    print("The result is: ", five(X, Y, Z))
elif action == "all":
    print("Input x, y, z, d, e")
    X = int(input())
    Y = int(input())
    Z = int(input())
    D = int(input())
    E = int(input())
    print("The result is: ", five(X, Y, Z, D, E))
else:
    print("INCORRECT INPUT!")
