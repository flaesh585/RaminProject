from tkinter import *
import tkinter.messagebox as box

def dialog():
    var = box.askyesno("Выбор действий", "Продолжаем ввод?")
    if var == 1:
        box.showinfo("Продолжение", "Продолжаем...")
    else:
        box.showwarning("Прекращение", "Выход...")

window = Tk()
window.title("Вывод сообщений")
window.geometry('500x300')
btn = Button(window, text='Выбор решения', bg="red", fg="#00ff00", width=20, font=("Arial", 16, "bold"), command=dialog)
btn.pack(padx=10, pady=10)
window.mainloop()