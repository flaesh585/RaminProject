from tkinter import *

window = Tk()
window.resizable(False, False)

frame_top = LabelFrame(window, text="Верхний ряд")
frame_bot = LabelFrame(window, text="Нижний ряд")

lab1 = Label(frame_top, width=8, height=3, bg='yellow', text='1')
lab2 = Label(frame_top, width=8, height=3, bg='red', text='2')
lab3 = Label(frame_bot, width=8, height=3, bg='lightgreen', text='3')
lab4 = Label(frame_bot, width=8, height=3, bg='lightblue', text='4')

frame_top.pack()
frame_bot.pack()

lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)
lab4.pack(side=LEFT)

window.mainloop()