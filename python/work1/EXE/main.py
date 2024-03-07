from tkinter import *
from tkinter import ttk

def calculate():
    try:
        first_value = float(first.get())
        second_value = float(second.get())
        operation = current_var.get()

        if operation == '+':
            result = first_value + second_value
        elif operation == '-':
            result = first_value - second_value
        elif operation == '*':
            result = first_value * second_value
        elif operation == '/':
            if second_value != 0:
                result = first_value / second_value
            else:
                result = "Ошибка: деление на ноль"
        
        # Выводим результат на окно программы
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")

window = Tk()
window.title("Калькулятор")
window.geometry("320x270")
window.resizable(False, False)
window.configure(bg='#F2C18D')

frame = Frame(window, bg='#F2C18D')
frame.pack(expand=1)


frame_top = Frame(frame)
first_label = Label(frame_top, text='Введите первое число: ', bg='#F2C18D')
first = Entry(frame_top, width=5)

frame_bott = Frame(frame)
second_label = Label(frame_bott, text='Введите второе число: ', bg='#F2C18D')
second = Entry(frame_bott, width=5)

current_var = StringVar()
operation_combobox = ttk.Combobox(frame, textvariable=current_var, width=3)
operation_combobox['values'] = ('+', '-', '*', '/')
operation_combobox.current(0)

btn = Button(frame, text='=', width=3, command=calculate)

result_label = Label(frame, text="", font=("Helvetica", 12, "bold"), bg='#F2C18D')

frame_top.pack()
first_label.pack(side=LEFT)
first.pack(side=LEFT)

operation_combobox.pack()

frame_bott.pack()
second_label.pack(side=LEFT)
second.pack(side=LEFT)

btn.pack()
result_label.pack()

window.mainloop()
  