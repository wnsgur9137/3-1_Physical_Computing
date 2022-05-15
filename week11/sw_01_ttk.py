import tkinter as tk
from tkinter import ttk

def change_duty(ev):
    lbl_pwm.configure(text='DUTY CYCLE : {}'.format(sb_pwm.get()))

def change_color():
    global pressed
    if pressed == False:
        c.itemconfig(cc, fill='red')
        pressed = True
    else:
        c.itemconfig(cc, fill='')
        pressed = False


pressed = False

root = tk.Tk()
root.geometry('400x300')

nb_tab = ttk.Notebook(root)
fr_tab1= ttk.Frame(nb_tab)
nb_tab.add(fr_tab1, text='PWM 제어')
fr_tab2= ttk.Frame(nb_tab)
nb_tab.add(fr_tab2, text='스위치 제어')

lbl_pwm = ttk.Label(fr_tab1, text='DUTY CYCLE')
led_v = tk.DoubleVar()
sb_pwm = tk.Scale(fr_tab1, label='LED', orient='h', from_=0, to=100, variable=led_v, command=change_duty)

c = tk.Canvas(fr_tab2, width=200, height=200)
c.pack()
cc = c.create_oval(50, 50, 150, 150, fill='')
btn_sw = ttk.Button(fr_tab2, text='스위치', command=change_color)
btn_sw.pack()

lbl_pwm.pack()
sb_pwm.pack(fill='x')
nb_tab.pack(fill='both')

root.mainloop()