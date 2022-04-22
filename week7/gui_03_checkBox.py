# v03
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def popup():
    # if checked.get() == False:
    if checked.get() == 0:  ####### 중요
        lbl_display.configure(text='체크버튼 OFF')
        messagebox.showinfo("언체크됨", "체크버튼 OFF")
    # elif checked.get() == True:
    elif checked.get() == 1:    ####### 중요
        lbl_display.configure(text='체크버튼 ON')
        messagebox.showinfo("언체크됨", "체크버튼 ON")
    else:
        lbl_display.configure(text="오류, 실행될 일 없음")
        messagebox.showerror("오류", "실행될 일 없음")

w = tk.Tk()
w.title('체크버튼 실습')
w.geometry('300x100')

# 파이썬에 기본 내장되어있긴 하지만, **파이썬으로 만든 라이브러리가 아니기에**, 타입을 설정 해준다.
# tk.IntVar(), tk.DoubleVar(), tk.StrVar(), tk.BooleanVar()
# tk.IntVar() -> 자바의 int가 아닌 Integer와 같다. (객체로 만든다.)
# 그렇기에 popup()의 if문에서 .get()을 사용할 수 있는 것이다.
# checked = tk.IntVar() # 정수형 변수 객체 지정
checked = tk.BooleanVar() # 논리형 변수 객체 지형
# checked = 0 # 기본 정수, get() 함수 등을 사용할 수 없다.

cb_on_off = tk.Checkbutton(w, text="출석체크", variable=checked, command=popup)
lbl_display = tk.Label(w, text='')
btn_dummy = tk.Button(w, text="더미버튼")
btn_dummy2 = ttk.Button(w, text="더미버튼") # ttk는 디자인(모양이 다름)

cb_on_off.pack()
lbl_display.pack()
btn_dummy.pack()
btn_dummy2.pack()

w.mainloop()