# BMI 계산 GUI 프로그램
# weight / (height * height)

import tkinter as tk

def bmi_change():
    try :
        height = float(en_height.get())
        weight = float(en_weight.get())
        bmi = weight / ((height/100)**2)
        if bmi >= 18.5 and bmi < 23 :
            stat = '정상'
        elif bmi >= 23 and bmi < 25 :
            stat = '과체중'
        elif bmi >= 25:
            stat = '비만'
        else :
            stat = '저체중'
        lbl_bmi.configure(text='당신의 bmi는 {0}이므로, {1}입니다.'.format(round(bmi, 2), stat))
    except ValueError as e:
        print('숫자만 입력해 주십시오. {0}'.format(e))
    except:
        print('오류 발생')


win = tk.Tk()
win.title('BMI 계산기')
win.geometry('1920x1080')

lbl_height = tk.Label(win, text="키를 입력해 주십시오.(cm)")
en_height = tk.Entry(win)
lbl_weight = tk.Label(win, text="몸무게를 입력해 주십시오(kg)")
en_weight = tk.Entry(win)
btn_change = tk.Button(win, text="변환", command=bmi_change)
lbl_bmi = tk.Label(win, text='BMI')

lbl_height.pack()
en_height.pack()

lbl_weight.pack()
en_weight.pack()
btn_change.pack()
lbl_bmi.pack()

en_height.focus()

win.mainloop()