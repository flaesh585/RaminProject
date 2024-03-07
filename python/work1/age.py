print("Input your age:", end=" ")
age = int(input())

if 0 <= age < 18:
	print("You are minor!")
elif 18 <= age <= 150:
	print("You are adult")
else:
	print("Input a correct age!")
