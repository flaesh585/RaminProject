from tkinter import *
window = Tk()
window.title('Фигуры произвольной формы')
#создаем холст
c = Canvas(window, width=450, height=250)
c.pack()
#рисуем треугольник
c.create_polygon((103.8, 83.34), (173, 27.78), (242.2, 83.34), fill='yellow', outline='red')
#рисуем трапецию
c.create_polygon((34.6, 166.68), (69.2, 111.12), (138.4, 111.12), (173, 166.68), fill='orange', outline='green')
#рисуем параллелипипед
c.create_polygon((242.2, 222.24), (242.2, 138.9), (380.6, 138.9), (380.6, 222.24), fill='red', outline='blue')
c.create_polygon((242.2, 138.9), (276.8, 111.12), (415.2, 111.12), (380.6, 138.9), fill='red', outline='blue')
c.create_polygon((380.6, 222.24), (380.6, 138.9), (415.2, 111.12), (415.2, 194.46), fill='red', outline='blue')
c.create_line((242.2, 222.24), (276.8, 194.46), dash=(3, 2), fill='blue')
c.create_line((276.8, 111.12), (276.8, 194.46), fill='blue', dash=(3, 2))
c.create_line((415.2, 194.46), (276.8, 194.46), fill='blue', dash=(3, 2))

window.mainloop()