from tkinter import *
window = Tk()
window.title('Сектор, сегмент и дуга круга')
c = Canvas(window, width=400, height=350)
c.pack()
#создадим сам круг
c.create_oval((66.68, 43.75), (333.4, 306.25), fill='lightgrey', outline='white')
#рисуем сегмент круга 90 градусов из точки 0 градусов
c.create_arc((66.68, 43.75), (333.4, 306.25), style=CHORD, start=90, extent=90, fill='red')
#рисуем сектор круга -45 градусов из точки 180 градусов
c.create_arc((66.68, 43.75), (333.4, 306.25), start=270, extent=-45, fill='orange')
#рисуем дугу круга -90 градусов из точки 75 градусов
c.create_arc((66.68, 43.75), (333.4, 306.25), style=ARC, outline='blue', width=4, start=30, extent=-90)
window.mainloop()