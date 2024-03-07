from tkinter import *
import tkinter.messagebox as box
#функция по выводу диалогового окна
def dialog():
    box.showinfo("Выбор языка", "Вы выбрали язык " + listbox.get(listbox.curselection()))

window = Tk() #создаем окно
window.title("Работа со списком")
frame = Frame(window)
#создаем виджет Listbox
listbox = Listbox(frame)
#заполняем список
for i in('Java', 'C++', 'Python', 'C#', 'JavaScript', 'PHP'):
    listbox.insert(END, i)
listbox.insert(3, "FORTRAN")
#создаем кнопку
btn = Button(frame, text="Выберите язык", bg="lightgreen", command=dialog)
#размещаем виджеты
btn.pack(side=RIGHT, padx=15)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()