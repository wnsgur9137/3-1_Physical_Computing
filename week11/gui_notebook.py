import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('300x200')

nb_tab = ttk.Notebook(root)
fr_tab1= ttk.Frame(nb_tab)
nb_tab.add(fr_tab1, text='PWM 제어')
fr_tab2= ttk.Frame(nb_tab)
nb_tab.add(fr_tab2, text='스위치 제어')

nb_tab.pack(fill='both')

root.mainloop()