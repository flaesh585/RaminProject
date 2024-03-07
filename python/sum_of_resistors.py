from tkinter import *

datalist = list()

def plus():
    value = lbl.get()
    datalist.append(value)
    lbl.delete(0, 'end')

def posled():
    result = 0
    for i in range(len(datalist)):
        result += float(datalist[i])
    otvet.configure(text=f"Результат: {result}")

def parallel():
    result = 0
    for i in range(len(datalist)):
        datalist[i] = 1 / float(datalist[i])
        result += float(datalist[i])
    otvet.configure(text=f"Результат: {result}")

window = Tk()
window.resizable(False, False)
window.configure(bg='#F7DED0')
window.geometry('550x400')
#создаём основной фрейм
frame = Frame(window, bg='#F7DED0')
frame.pack(expand=1)
#создаём вверхний фрейм
frame_top = Frame(frame, bg='#F7DED0')
frame_top.pack(side=TOP)
#создаём поле для вывода результата
otvet = Label(frame_top, text="Результат: ", bg='#F7DED0', font="Arial 18")
otvet.pack(side=TOP)
#создаём фрейм-коробку для поля ввода и кнопки +
box = Frame(frame_top, bg='#F7DED0')
box.pack(expand=1)
#создаём нижний фрейм
frame_bottom = Frame(frame, bg='#F7DED0')
frame_bottom.pack()
#создаём кнопку+ и поле ввода
plus_btn = Button(box, text='+', bg='#FEECE2', relief=RIDGE, activebackground='#E2BFB3', command=plus)
lbl = Entry(box, width=12)
lbl.pack(side=LEFT)
plus_btn.pack(side=LEFT)
#создаём нижнюю часть
parall_btn = Button(frame_bottom, text='паралл', bg='#FEECE2', relief=RIDGE, activebackground='#E2BFB3', height=2, width=10, command=parallel)
posl_btn = Button(frame_bottom, text='послед', bg='#FEECE2', relief=RIDGE, activebackground='#E2BFB3', height=2, width=10, command=posled)
parall_btn.pack(side=LEFT)
posl_btn.pack(side=RIGHT)


window.mainloop()