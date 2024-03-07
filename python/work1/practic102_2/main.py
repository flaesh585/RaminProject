import os

print("Hi! What's your name?")
try:
    answer = input()
except ValueError:
    print("Incorrect input!")

with open(os.path.join("practic102_2", "answer.txt"), "w+") as f:
    f.write(answer)