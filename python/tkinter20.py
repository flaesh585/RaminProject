from tkinter import *

window = Tk()

class MyButton:
    def __init__(self):
        self.btn = Button(text="Обработка", width=20, height=3, font=("Arial", 14, "bold"))
        self.btn.bind('<Button-1>', self.change)
        self.btn.bind('<Return>', self.change)
        self.btn.pack()

    def change(self, event):
        self.btn['bg'] = "yellow"
        self.btn['fg'] = "blue"

MyButton()

window.mainloop()
