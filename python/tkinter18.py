from tkinter import *
window = Tk()
window.title("Меню с выпадающим списком")
#создаем меню в главном окне
mainmenu = Menu(window)
window.config(menu=mainmenu)
#создаем пункты подменю для пункта меню "Файл"
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")
#создаем пункты подменю для пункта меню "Справка"
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
#связываем два созданных меню с главным меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

window.mainloop()