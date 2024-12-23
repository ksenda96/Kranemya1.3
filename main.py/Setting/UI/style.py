from tkinter import *
from tkinter import ttk


style = ttk.Style()
style.theme_use('classic')
style.configure('TNotebook.Tab',
                background="#1c75ff",
                wgt="#1c75ff")
style.configure('TNotebook',
                background="#1c75ff")
style.configure('TFrame',
                background="#1c75ff")
style.map('TNotebook.Tab',
          background=[("pressed",
                       "!disabled",
                       "#1c75ff"),
                      ("active",
                       "#1c75ff")])
style.map('TButton',
          background=[("pressed",
                       "!disabled",
                       "#1c75ff"),
                      ("active",
                       "#1c75ff")])

ttk.Style().theme_use("classic")







loadimagebnt00 = PhotoImage(file='image/main.png')
loadimagebnt01 = PhotoImage(file='image/group.png')
loadimagebnt02 = PhotoImage(file='image/Friends.png')
loadimagebnt03 = PhotoImage(file='image/message.png')
loadimagebnt04 = PhotoImage(file='image/sms.png')
loadimagebnt05 = PhotoImage(file='image/attach.png')
loadimagebnt06 = PhotoImage(file='')
loadimagebnt07 = PhotoImage(file='')
loadimagebnt08 = PhotoImage(file='')
loadimagebnt09 = PhotoImage(file='')
loadimagebnt1 = PhotoImage(file='')