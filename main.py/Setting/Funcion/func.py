import tkinter
from dataclasses import fields
from tkinter import *
from tkinter import ttk
from Setting.Funcion import book
from Setting.UI import root
from Setting.UI.style import loadimagebnt04, loadimagebnt05






#FRAME0
#Friends, Group, Message
def config(lbt1=None):
    ltb1 = (Listbox(book.frame0,
                    xscrollcommand=txt1,
                    bg='#1c75ff')
            .place(relx=0.0443,
                   rely=0,
                   relwidth=0.3,
                   relheight=1))

def config1():
    ltb2 = (Listbox(book.frame0,
                    bg='#1c75ff')
            .place(relx=0.0443,
                   rely=0,
                   relwidth=0.3,
                   relheight=1))


def config2():
    ltb3 = (Listbox(book.frame0,
                    bg='#1c75ff')
            .place(relx=0.0443,
                   rely=0,
                   relwidth=0.3,
                   relheight=0.85))
    ent0 = (Entry(book.frame0,
                 bd=2, bg='#1c75ff')
            .place(relx=0.0441,
                   rely=0.852,
                   relwidth=0.271,
                   relheight=0.099))
    btn31 = (Button(book.frame0,
                   bd=0,
                    bg='#1c75ff',
                   image=loadimagebnt04,command=sms)
             .place(relx=0.315,
                    rely=0.852,
                    relwidth=0.03,
                    relheight=0.05))
    btn32 = (Button(book.frame0,
                   bd=0,
                   bg='#1c75ff',
                   image=loadimagebnt05)
             .place(relx=0.315,
                    rely=0.9,
                    relwidth=0.03,
                    relheight=0.051))




#Listbox1,2,3
def txt1(listbox=None, *args):
    txt = Text()

def sms(ltb3=None, ent0=None):
    ltb3.delete(0, "end")
    for i in range(len(fields)):
        ltb3.insert("end", ent0[i].get())
