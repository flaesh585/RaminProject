from tkinter import *

window = Tk()
window.title("Обработка разных событий")

#функция обработчик для нескольких событий
def change_color(col):
    lb['fg'] = col

#создаем метку
lb = Label(text="Обработка разных событий")
lb.pack()
#создаем кнопку окрашивающую текст в синий цвет, и сразу размещаем его
Button(command=lambda col='Blue':change_color(col)).pack()
#создаем кнопку окрашивающую текст в красный цвет, и сразу размещаем его
Button(command=lambda col='red':change_color(col)).pack()

window.mainloop()