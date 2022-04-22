# v04
import tkinter as tk
from tkinter import ttk

def popup():
    if selected.get() == 0:
        lbl_display.configure(image=p1)
    elif selected.get() == 1:
        lbl_display.configure(image=p2)
    elif selected.get() == 2:
        lbl_display.configure(image=p3)

w = tk.Tk()
w.title('체크버튼 실습')
w.geometry('500x500')

selected = tk.IntVar() # 중요

p1 = tk.PhotoImage(file='michael.PNG')
p2 = tk.PhotoImage(file='franklin.PNG')
p3 = tk.PhotoImage(file='trevor.PNG')

rb_1 = ttk.Radiobutton(w, text="마이클", command=popup, variable=selected, value=0) # value 중요
rb_2 = ttk.Radiobutton(w, text="프랭클린", command=popup, variable=selected, value=1)
rb_3 = ttk.Radiobutton(w, text="트래버", command=popup, variable=selected, value=2)

lbl_display = ttk.Label(w, text="선택할 플레이어는?")

# lbl_display.pack()
# rb_1.pack(side='left')
# rb_2.pack(side='left')
# rb_3.pack()

lbl_display.configure(image=p1) # 처음 이미지

rb_1.grid(row=0, column=0)
rb_3.grid(row=0, column=1)
rb_2.grid(row=0, column=2)
lbl_display.grid(row=1, column=0, columnspan=3)

w.mainloop()