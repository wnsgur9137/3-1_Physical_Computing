# v02 Message
import tkinter as tk
from tkinter import messagebox

def popup(): # message
    # showinfo -> 정보 메세지
    # messagebox.showinfo("클릭", "버튼이 눌렸습니다.")

    # showwarning -> 경고 메세지
    # messagebox.showwarning("클릭", "버튼이 눌렸습니다.")

    # showerror -> 에러 메세지
    # messagebox.showerror("클릭", "버튼이 눌렸습니다.")

    # askyesnocancel -> yes, no, cancel
    messagebox.askyesnocancel("클릭", "버튼이 눌렸습니다.")

w = tk.Tk()
w.title('세 번째 GUI 프로그램')
# w.geometry('300x100')

# 이미지 준비
p1 = tk.PhotoImage(file='michael.PNG')
p2 = tk.PhotoImage(file='franklin.PNG')
p3 = tk.PhotoImage(file='trevor.PNG')

# 이미지 및 버튼에 상요할 이미지 바인딩
lbl_display1 = tk.Label(w, image=p1)
lbl_display2 = tk.Label(w, image=p2)
btn_display3 = tk.Button(w, image=p3, command=popup)

# 위젯 배치
lbl_display1.pack(side='left')
lbl_display2.pack(side='left')
btn_display3.pack()

w.mainloop()