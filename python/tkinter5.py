from tkinter import *
window = Tk()
window.geometry('500x300')
window.resizable(False, False)
window.title('Experiment Project!')

label = Label(window, bg='blue', fg='yellow', font='Arial 16', text='vscxcs')

label.pack(anchor=NW)

window.mainloop()