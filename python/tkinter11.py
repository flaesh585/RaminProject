from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Ввод данных")
frame = Frame(window)
entry = Entry(frame)

def dialog():
    box.showinfo("Приветствие", "Привет, " + entry.get())

btn = Button(frame, text="Ввод", command=dialog)
lb = Label(frame, text="Введите имя: ")
lb.pack(side=LEFT)
entry.pack(side=LEFT)
btn.pack(side=RIGHT, padx=5)
frame.pack(padx=20, pady=20)

window.mainloop()