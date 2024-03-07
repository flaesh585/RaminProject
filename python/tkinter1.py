from tkinter import * 

window = Tk()
window.geometry('270x320')
window.title('Experiment Project')
#Create one 
lab1 = Label(width=8, height=3, bg='yellow', text="1")
lab2 = Label(width=8, height=3, bg='red', text="2")
lab3 = Label(width=8, height=3, bg='lightgreen', text="3")
lab4 = Label(width=8, height=3, bg='lightblue', text="4")

#Распологаем метки вертикально сверху вниз
lab1.pack(side=RIGHT)
lab2.pack(side=RIGHT)
lab3.pack(side=RIGHT)
lab4.pack(side=RIGHT)

window.mainloop()