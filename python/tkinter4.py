from tkinter import *

window = Tk()
window.resizable(False, False)
window.title('Вывод текста')
window.geometry('500x300')

label = Label(window, bg='blue', fg='yellow', text='SPBGAU', font='Arial 16')
label.pack(expand=1, fill=Y)

window.mainloop()