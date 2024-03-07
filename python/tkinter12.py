from tkinter import *

window = Tk()
window.title("Многострочный текст")
text = Text(width=30, height=10, bg="blue", fg="yellow", wrap=WORD)
text.pack()

window.mainloop()