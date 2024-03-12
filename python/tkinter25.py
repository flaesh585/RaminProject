from tkinter import *

window = Tk()
window.title('прямоугольник')
c = Canvas(window, width=300, height=200)
c.pack()
c.create_rectangle(20, 20, 280, 40, outline='red')
c.create_rectangle(100, 60, 200, 180, fill='yellow', outline='green', activedash=(5, 4))

window.mainloop()