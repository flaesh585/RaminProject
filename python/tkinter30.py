from tkinter import *

window = Tk()
window.title('Игра в прямоугольник')

canvas = Canvas(window, width=400, height=200)
canvas.focus_set()
canvas.pack()

rect = canvas.create_rectangle()