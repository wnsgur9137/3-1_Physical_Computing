# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
#
# def popup() :
#     # if checked.get() == false:
#     if checked.get() == 0 :
#         lbl_display.configure(text='체크버튼 OFF')
#         messagebox.showinfo('언체크됨', '체크버튼 OFF')
#     elif checked.get() == 1:
#         lbl_display.configure(text='체크박스 ON')
#         messagebox.showinfo('체크됨', '체크버튼 ON')
#     else :
#         lbl_display.configure(text='오류, 실행될 일 없음')
#         messagebox.showerror('오류', '실행될 일 없음')
#
#
# w = tk.Tk()
# w.title('체크버튼 실습')
# w.geometry('300x100')
#
# checked = tk.BooleanVar()
#
# cb_on_off = tk.Checkbutton(w, text='출석체크', variable=checked, command=popup)
# lbl_display = tk.Label(w, text='')
#
# # cb_on_off.grid(row=0, column=0)
# # lbl_display.grid(row=1, column=1)
#
# cb_on_off.pack()
# # lbl_display.pack()
#
# # lbl_display.grid(row=0, column=0)
#
# w.mainloop()


# import tkinter as tk
#
# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
# # w.geometry('300x100')
#
# p1 = tk.PhotoImage(file='../week7/michael.png')
# p2 = tk.PhotoImage(file='../week7/franklin.png')
# p3 = tk.PhotoImage(file='../week7/trevor.PNG')
#
# lbl_display1 = tk.Label(w, image=p1)
# lbl_display2 = tk.Label(w, image=p2)
# lbl_display3 = tk.Label(w, image=p3)
#
# lbl_display1.pack(side='left')
# lbl_display2.pack(side='left')
# lbl_display3.pack()
#
# w.mainloop()



import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def popup():
    messagebox.askyesnocancel('클릭', '버튼이 눌렸습니다.')

w = tk.Tk()
w.title('메세지 박스 연습')
# w.geometry('300x100')

p1 = tk.PhotoImage(file='../week7/michael.PNG')
p2 = tk.PhotoImage(file='../week7/franklin.PNG')
p3 = tk.PhotoImage(file='../week7/trevor.PNG')

lbl_display1 = tk.Button(w, image=p1, command=popup)
lbl_display2 = tk.Button(w, image=p2, command=popup)
lbl_display3 = tk.Button(w, image=p3, command=popup)

lbl_display1.pack(side='left')
lbl_display2.pack(side='left')
lbl_display3.pack(side='left')

w.mainloop()