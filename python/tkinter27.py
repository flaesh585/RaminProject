from tkinter import *
window = Tk()
window.title('Эллипсы')
c = Canvas(window, width=250, height=2000)
c.pack()
c.create_oval((73.5, 20), (161.7, 120), outline='red')
c.create_oval((44.1, 140), (191.1, 180), outline='white', fill='grey80')

window.mainloop()