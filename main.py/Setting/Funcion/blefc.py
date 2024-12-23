from tkinter import *
from tkinter import ttk
from Setting.Funcion import book
from Setting.Funcion.book import root
from Setting.Funcion.func import config, config1, config2
from Setting.UI.style import loadimagebnt01, loadimagebnt02, loadimagebnt03
from Setting.UI.style import style




btn1 = (Button(book.frame0,
               image=loadimagebnt01,
               command = config,
               bg='#1c75ff')
        .place(relx=0.0001,
               rely=0,
               relwidth=0.04,
               relheight=0.06))
btn2 = (Button(book.frame0,
             image=loadimagebnt02,
              bg='#1c75ff')
       .place(relx=0.0001,
              rely=0.061,
              relwidth=0.04,
              relheight=0.06))
btn3 = (Button(book.frame0,
             image=loadimagebnt03,
             command=config2,
              bg='#1c75ff')
       .place(relx=0.0001,
              rely=0.122,
              relwidth=0.04,
              relheight=0.06))
srr = (ttk.Separator(book.frame0,
                    orient='vertical')
       .place(relx=0.042,
              rely=0,
              relwidth=0.001,
              relheight=1))

#*****************************************************************************

