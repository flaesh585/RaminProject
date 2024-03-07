def funct(x):
    return float(x)

giris = str(input("Input your text\n"))

try:
    print(funct(giris))
    
except(ValueError, SyntaxError):
    print("Incorrect value")
    
