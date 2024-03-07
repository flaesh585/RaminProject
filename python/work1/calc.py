num1 = int(input())
num2 = int(input())
oper = str(input())
suma = 0
prod = 1

if oper == "+":
    suma = num1 + num2
elif oper == '-':
    suma = num1 - num2
elif oper == '*':
    prod = num1 * num2
elif oper == '/':
    prod = num1 / num2
elif oper == '^':
    prod = num1 ** num2

#вывод результатов

if (prod == 1) and suma != 0:
    print('Сумма: ', suma)
else:
    print('Произведение: ', prod)