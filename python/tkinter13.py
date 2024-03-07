from tkinter import *
window = Tk()
window.title("Полоса прокрутки")
#Создаем многострочное поле ввода
text = Text(width=30, height=5, bg="black", fg="green", wrap=WORD)
text.pack(side=LEFT)
#создаем вертикальную полосу прокрутки
scroll = Scrollbar(orient=VERTICAL, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
#конфигурируем поле ввода с полосой прокруткой
text.config(yscrollcommand=scroll.set)
window.mainloop()