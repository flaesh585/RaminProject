from tkinter import *

window = Tk()
window.title("Меню с разделенными подменю")
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Открыть...")
filemenu.add_separator()
filemenu.add_command(label="Новый")
filemenu.add_separator()
filemenu.add_command(label="Сохранить...")
filemenu.add_separator()
filemenu.add_command(label="Выход")

helpmenu = Menu(mainmenu, tearoff=0)

helpmenu.add_command(label="Локальная справка")
helpmenu.add_separator()
helpmenu.add_command(label="На сайте")
helpmenu.add_separator()
helpmenu.add_command(label="Помощь")
helpmenu.add_separator()
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

window.mainloop()