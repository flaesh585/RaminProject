print("Введите число:", end=" ")
num = int(input())

if num <= 10:
	print("меньше или равно 10")
elif num > 10 and num <= 25:
	print("больше 10 и  меньше либо равно 25")
elif num > 25:
	print("больше 25")
else:
	print("неправильный формат")