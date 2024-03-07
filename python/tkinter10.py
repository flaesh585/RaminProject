from tkinter import *
from tkinter import filedialog as fd

def insertText():
    file_name = fd.askopenfilename() #получаем имя файла
    a = open(file_name)
    s = a.read()
    text.insert(1.0, s)
    a.close() #закрываем файл
    
def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("ALL files", "*.*") ))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

window = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)

#Цикл обработки событий окна
window.mainloop()