import tkinter as tk
import random

b3 = ['송민섭', '간명해', '이교범','김준영','김현호','조민호','전유진','강성모','고대현','김광래','임진수','김주연','한승민','황태결','이준용']



def plus():
    """ 더하기 버튼 """
    try:
        a = int(en_input.get())
        b = int(en_input2.get())
        res = a + b
        lbl_result.configure(text=f'{a}+{b}={res}')
    except Exception as e:
        lbl_result.configure(text=f'{e}')
        en_input.delete(0, 'end')
        en_input2.delete(0, 'end')

def div():
    """ 나누기 버튼 """
    try:
        a = int(en_input.get())
        b = int(en_input2.get())
        res = a / b
        lbl_result.configure(text=f'{res}')
    except ZeroDivisionError as e:
        lbl_result.configure(text=f'분모에 0 이 올 수 없습니다.\n{e}')
    except Exception as e:
        lbl_result.configure(text=f'{e}')
        en_input.delete(0, 'end')
        en_input2.delete(0, 'end')

def rando():
    try:
        a = random.randint(0,9)
        b = random.randint(0,9)
        p = a+b
        d = a/b
        lbl_result.configure(text=f'첫 번째 수 : {a} 두 번째 수 : {b}\n더하기 결과 : {p} 나누기 결과 : {d}')
    except ZeroDivisionError as e:
        lbl_result.configure(text=f'분모에 0 이 올 수 없습니다.\n{e}')
    

def nrd():
    dic = {}
    for name in b3 :
        rn = random.randint(1,100)
        dic[name] = rn
    with open("quiz.txt", 'w', encoding='utf-8') as fp:
        for k,v in dic.items():
            print(f'{k} {v}',file=fp) # 실제 쓰기
        lbl_result.configure(text='Quiz 파일 생성 완료!')
    

    


if __name__ == '__main__':
    w = tk.Tk()
    w.title('SMS_201744101.py')
    w.geometry('500x300')

    en_input = tk.Entry(w)
    en_input2 = tk.Entry(w)
    btn_plus = tk.Button(w, text='더하기', command=plus)
    btn_div = tk.Button(w, text='나누기', command=div)
    btn_rand = tk.Button(w,text='랜덤번호 (각각 0~9 사이의 수)', command=rando)
    btn_nrd = tk.Button(w, text='성명, 랜덤번호', command=nrd)
    lbl_result = tk.Label(w, text='결과창')

    en_input.pack(fill='x')
    en_input2.pack(fill='x')
    btn_plus.pack(fill='x')
    btn_div.pack(fill='x')
    btn_rand.pack(fill='x')
    btn_nrd.pack(fill='x')
    lbl_result.pack()

    en_input.focus()

    w.mainloop()


# 레이아웃 배치는 3가지 (pack, greed, place)
