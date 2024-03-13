from tkinter import *

window = Tk()
window.title('Структура инвестиционного портфеля')
c = Canvas(window, width=500, height=200)
c.pack()

c.create_arc((10, 10), (190, 190), start=0, extent=72, fill='blue')
c.create_arc((10, 10), (190, 190), start=72, extent=288, fill='red')

c.create_rectangle((250, 100), (300, 120), fill='blue')
c.create_rectangle((250, 150), (300, 170), fill='red')

c.create_text((350, 50), text="Круговая диаграмма", justify=CENTER, fill='green', font="Times 14 bold")
c.create_text((325, 110), text="Лукойл - 20%", anchor=W, fill='darkgreen', font='Times 10 bold')
c.create_text((325, 160), text="Сбербанк - 80%", anchor=W, fill='darkgreen', font="Times 10 bold")

window.mainloop()
