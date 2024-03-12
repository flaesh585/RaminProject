from tkinter import *
#создаем окно
window = Tk()
window.title('Линии')
#Создаем холст
c = Canvas(window, width=200, height=200, bg='yellow')
c.pack()
#создаем сплошную линию
c.create_line(20, 15, 150, 45, width=3, fill='red')
#создаем линию со стрелкой
c.create_line(100, 180, 100, 60, fill='green', width=5, arrow=LAST, dash=(10, 2), arrowshape="10 20 10")
window.mainloop()