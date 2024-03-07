from tkinter import *
import tkinter.messagebox as box
#функция по выводу диалогового окна
def dialog():
    box.showinfo("Выбор языка", "Вы выбрали язык " + book.get())

window = Tk()
window.title("Работа с переключателем")
#создаем фрейм для виджетов
frame = Frame(window)
#Создаем строковую переменную-обьект для хранения результата выбора
book = StringVar()
#создаем виджеты положения переключателя
r_1 = Radiobutton(frame, text="Java", variable=book, value="Java")
r_2 = Radiobutton(frame, text="C++", variable=book, value="C++")
r_3 = Radiobutton(frame, text="Python", variable=book, value="Python")
r_4 = Radiobutton(frame, text="FORTRAN", variable=book, value="FORTRAN")
r_5 = Radiobutton(frame, text="C#", variable=book, value="C#")
r_6 = Radiobutton(frame, text="JavaScript", variable=book, value="JavaScript")
r_7 = Radiobutton(frame, text="PHP", variable=book, value="PHP")
#устанавливаем переключатель в первое положение
r_1.select()
#создаем кнопку
btn = Button(frame, text="Выберите язык", bg="lightgreen", command=dialog)
#размещаем виджеты
r_1.pack(padx=10)
r_2.pack(padx=10)
r_3.pack(padx=10)
r_4.pack(padx=10)
r_5.pack(padx=10)
r_6.pack(padx=10)
r_7.pack(padx=10)
btn.pack()
frame.pack(padx=120, pady=30)

window.mainloop()