import tkinter as tk

def f2c():  # (32°F − 32) × 5/9 = 0°C
    try:
        f = float(en_input.get())
        c = (f - 32.0) * (5.0/9.0)
        lbl_temp.configure(text='화씨 {0}도는 섭씨 {1}도 입니다.'.format(f, round(c, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해 주십시오.\n{0}'.format(e))
    finally:
        en_input.delete(0, 'end')
    # lbl_temp.configure(text=round(c, 4))
    # print('버튼 클릭됨.' + f)
    # print(1 + f) # -> typeError

def f2c_enter(ev):
    f2c()

def c2f():
    try:
        c = float(en_input.get())
        f = (c * (9/5)) + 32
        lbl_temp.configure(text='섭씨 {0}도는 섭씨{0}도 입니다.'.format(c, round(f, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해 주십시오.\n{0}'.format(e))
    finally:
        en_input.delete(0, 'end')

w = tk.Tk()
w.title('두 번째 GUI 프로그램')
w.geometry('300x100')

en_input = tk.Entry(w)
btn_f2c = tk.Button(w, text='화씨 -> 섭씨', command=f2c)  # 콜백 함수(정수나 실수같은 객체가 아닌 함수의 이름(메모리 번지 주소)을 던진다.)
btn_change = tk.Button(w, text='화씨, 섭씨 변경')
lbl_temp = tk.Label(w, text='온도 변환 프로그램')

# 바인드 (키)
en_input.bind('<Return>', f2c_enter) # 함수를 하나 더 생성해도 되고, 람다함수

en_input.pack()
btn_f2c.pack()
lbl_temp.pack()

en_input.focus()

w.mainloop()
