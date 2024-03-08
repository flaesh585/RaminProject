from tkinter import *

window = Tk()
window.title("Работа с меню")
#создаем еню в главном окне
mainmenu = Menu(window)
#добавляем пункты меню
mainmenu.add_command(label="Файл")
mainmenu.add_command(label="Справка")
#конфигурируем окно с меню
window.config(menu=mainmenu)
window.mainloop()