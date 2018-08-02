from tkinter import *
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
from tkinter.filedialog import *
import os
from tkFontChooser import askfont

root=Tk()
root.title("Notepad")
root.geometry("500x300+100+100")

def show():
    print("Any item clicked")

def open1():
    file=tkinter.filedialog.askopenfile()
    print(file)
    filename=file.name
    f = open(filename)
    textarea.insert(INSERT,f.read())

def color():
        color = tkinter.colorchooser.askcolor()
        textarea.config(bg=color[1])

def color1():
        color= tkinter.colorchooser.askcolor()
        textarea.config(fg=color[1])

def callback():
    font=askfont(root)
    if font:
        font['family']=font['family'].replace(' ','\ ')
        font_str="%(family)s %(size)i %(weight)s %(slant)s" % font
        if font['underline']:
            font_str +='underline'
        if font['overstrike']:
            font_str +='overstrike'
        textarea.config(font=font_str)

def exit():
    root.destroy()

def new():
    a = tkinter.messagebox.askyesnocancel(title="Titlebar", message="Do you want to exit??")
    if(a==True):
        save1()
    elif(a==FALSE):
        root.title("Notepad")
        textarea.delete(0.0, END)
    else:
        textarea

def save1(filename=None):
    if filename == None:
        filename = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if filename == "":
            filename = None
        else:

            file = open(filename, "w")
            file.write(textarea.get(1.0, END))
            file.close()
            root.title(os.path.basename(filename) + " Notepad")

    else:
        file = open(filename, "w")
        file.write(textarea.get(1.0, END))
        file.close()

def cut():
       textarea.event_generate("<<Cut>>")

def copy():
        textarea.event_generate("<<Copy>>")

def paste():
        textarea.event_generate("<<Paste>>")

def about1():
    tkinter.messagebox.showinfo(title="About", message="Created by: Rahul Raj")


mymenu=Menu()
list1=Menu()
list1.add_command(label="New",command=new)
list1.add_command(label="Open",command=open1)
list1.add_command(label="Save",command=save1)
list1.add_command(label="---------------")
list1.add_command(label="Exit",command=exit)


list2=Menu()
list2.add_command(label="cut",command=cut)
list2.add_command(label="copy",command=copy)
list2.add_command(label="paste",command=paste)



list4=Menu()
list4.add_command(label="Font",command=callback)
list3=Menu(mymenu)
list3.add_command(label="Background Color",command=color)
list3.add_command(label="Foreground Color",command=color1)
list4.add_cascade(label="Color Chooser",menu=list3)

mymenu.add_cascade(label="File",menu=list1)
mymenu.add_cascade(label="Edit",menu=list2)
mymenu.add_cascade(label="Format",menu=list4)
mymenu.add_cascade(label="About Notepad",command=about1)

scroll=Scrollbar()
scroll.pack(side=RIGHT,fill=Y)

textarea=Text(bg="white",fg="blue",width=300,height=500)
textarea.pack()

scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


root.config(menu=mymenu)

root.mainloop()