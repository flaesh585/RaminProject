def color_switch():
    if window.cget('bg') == "yellow":
        window.configure(bg="green")
    else:
        window['bg']="yellow"

from tkinter import *
window = Tk()
window.geometry('500x300')
window.resizable(False, False)
window.title('Work with buttons')

btn_exit = Button(window, text='Exit', bg='#ff0000', fg='green', width=12, command=exit)
btn_switch = Button(window, text='Switch', bg="blue", fg="red", width=15, font=("Arial", 16, "bold"), command=color_switch)

btn_switch.pack(padx=150, pady=50)
btn_exit.pack(padx=150, pady=20)

window.mainloop()