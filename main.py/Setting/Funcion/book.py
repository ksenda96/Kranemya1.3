import os
from tkinter import *
from tkinter import ttk
from Setting.Funcion.func import config
from tkinter.ttk import Notebook, Style
from Setting.Funcion import blefc
from Setting.UI.style import loadimagebnt00
from Setting.UI.style import style



root = ttk.Notebook()
root.pack(expand=True, fill=BOTH)
frame0 = ttk.Frame(root)
frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame3 = ttk.Frame(root)
frame0.pack(fill=BOTH, expand=True)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
root.add(frame0, image=loadimagebnt00, compound=LEFT)
root.add(frame1, text="1", compound=LEFT)
root.add(frame2, text="1", compound=LEFT)
root.add(frame3, text="1", compound=LEFT)