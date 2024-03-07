from tkinter import *

window = Tk()
window.resizable(False, False)

frame_top = Frame(window)
frame_bot = Frame(window)

lab1 = Label(frame_top, width=8, height=3, bg='yellow', text='1')
lab2 = Label(frame_top, width=8, height=3, bg='red', text='2')
lab3 = Label(frame_bot, width=8, height=3, bg='lightgreen', text='3')
lab4 = Label(frame_bot, width=8, height=3, bg='lightblue', text='4')
#распологаем фреймы один под другим
frame_top.pack()
frame_bot.pack()
#распологаем метки во фреймах слева направо
lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)
lab4.pack(side=LEFT)
#зацикливаем
window.mainloop()