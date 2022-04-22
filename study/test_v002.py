
# 안주 추천 프로그램 연습
# 1. alcohol_foods 딕셔너리 사용
# 2. 각 술의 이미지를 가진 버튼들을 생성
# 3. 각 버튼을 클릭하면 주문이 완료되었다는 안내 메세지 출력
# 3-1. 각 버튼을 클릭하면 bill.txt에 주문내역 로그 남기기
# 4. 결제 방식을 radio 버튼으로 선택
# 5. 결제 버튼을 누를 시 bill.txt에 로그를 저장하고 결제완료 안내메세지 출력
# 6. 각 안주들을 페이징 처리하여 두 개씩 출력
# 7. 키보드 A를 누르면 페이징 '이전', 키보드 D를 누르면 페이징 '다음'


import tkinter as tk
import random
import datetime as dt
from tkinter import ttk
from tkinter import messagebox

alcohol_foods = {'맥주':['치킨', 20000],
                 '와인':['치즈', 5000],
                 '고량주':['짬뽕', 8000],
                 '소주':['골뱅이소면', 9000]}

# messagebox의 askyesno는 안배운 내용
def choice_foods(alcohol):
    choice = messagebox.askyesno('주문', '{0}의 추천 안주는 {1}입니다.\n가격은 {2}원 입니다.\n주문하시겠습니까?'
                                 .format(alcohol, alcohol_foods[alcohol][0], alcohol_foods[alcohol][1]))
    if choice == True:
        messagebox.showinfo('주문완료', '주문이 완료되었습니다.')
        lbl_total.configure(text='{0} 주문, 추천 안주는 {1} 가격 {2}'
                            .format(alcohol, alcohol_foods[alcohol][0], alcohol_foods[alcohol][1]))
        print('{0} 주문, 추천 안주는 {1} 가격 {2}'
                .format(alcohol, alcohol_foods[alcohol][0], alcohol_foods[alcohol][1]), file=fp)
    else:
        messagebox.showinfo('주문취소', '주문이 취소되었습니다.')


def select_beer():
    choice_foods('맥주')


def select_wine():
    choice_foods('와인')


def select_kaoliang():
    choice_foods('고량주')


def select_soju():
    choice_foods('소주')


def select_random():
    alcohol_foods_list = list(alcohol_foods)
    print('아무거나 선택 : ', end='', file=fp)
    any = random.choice(alcohol_foods_list)
    choice_foods(any)


def select_pay():
    if selected_payment.get() == 0:
        payment = '현금'
    else :
        payment = '카드'
    choice = messagebox.askyesno('결제', '{0} 방식으로 결제하시겠습니까?'.format(payment))
    if choice == True:
        messagebox.showinfo('결제완료', '결제가 완료되었습니다.')
        print('{0} 방식으로 결제가 완료되었습니다.'.format(payment), file=fp)
    else:
        messagebox.showinfo('결제취소', '결제가 취소되었습니다.')


def img_set(text):  # 안배운 내용(쓸모도 없음)

    str_img = './resources/'
    if(text == 'beer'):
        str_img += 'beer.png'
    elif(text == 'wine'):
        str_img += 'wine.png'
    elif(text == 'kaoliang'):
        str_img += 'kaoliang.png'
    elif(text == 'soju'):
        str_img += 'soju.png'
    elif(text == 'random'):
        str_img += 'random.png'
    elif(text == 'chicken'):
        str_img += 'chicken.png'
    elif(text == 'cheese'):
        str_img += 'cheese.png'
    elif(text == 'champon'):
        str_img += 'champon.png'
    elif(text == 'golbangi'):
        str_img += 'golbangi.png'
    return str_img


def click_prev():
    global idx, idx2
    idx = idx - 1
    idx2 = idx2 - 1
    if idx < 0:
        idx = len(foods_list) -1
    if idx2 < 0:
        idx2 = len(foods_list) - 1
    lbl_foods_img1.configure(image=foods_list[idx])
    lbl_foods_img2.configure(image=foods_list[idx2])


def click_next():
    global idx, idx2
    idx = idx + 1
    idx2 = idx2 + 1
    if idx > len(foods_list) - 1:
        idx = 0
    if idx2 > len(foods_list) - 1:
        idx2 = 0
    lbl_foods_img1.configure(image=foods_list[idx])
    lbl_foods_img2.configure(image=foods_list[idx2])


def finish():   # 안배운 내용
    choice = messagebox.askyesno('종료', '프로그램을 종료하시겠습니까?')
    if choice == True:
        win.destroy()


def key_down(event):    # 안배운 내용
    # key = event.keycode
    sym = event.keysym
    if sym == 'Left' or sym == 'a':
        click_prev()
    if sym == 'Right' or sym == 'd':
        click_next()


def pg_dw(event):
    click_prev()

def pg_up(event):
    click_next()


if __name__ == '__main__' :
    # tk init
    # -----------------------------------
    win = tk.Tk()
    win.title("안주 추천 프로그램")
    # win.geometry('1200x800')
    # -----------------------------------

    # Image
    # -----------------------------------
    img_beer = tk.PhotoImage(file=img_set('beer'))
    img_wine = tk.PhotoImage(file=img_set('wine'))
    img_kaoliang = tk.PhotoImage(file=img_set('kaoliang'))
    img_soju = tk.PhotoImage(file=img_set('soju'))
    img_random = tk.PhotoImage(file=img_set('random'))

    img_chicken = tk.PhotoImage(file=img_set('chicken'))
    img_cheese = tk.PhotoImage(file=img_set('cheese'))
    img_champon = tk.PhotoImage(file=img_set('champon'))
    img_golbangi = tk.PhotoImage(file=img_set('golbangi'))
    # -----------------------------------


    # 안주 이미지 페이징 처리를 위한 리스트와 변수
    # -----------------------------------
    foods_list = [img_chicken, img_cheese, img_champon, img_golbangi]
    idx = 0
    idx2 = 1
    # -----------------------------------


    # Button
    # -----------------------------------
    btn_beer = tk.Button(win, image=img_beer, command=select_beer)
    btn_wine = tk.Button(win, image=img_wine, command=select_wine)
    btn_kaoliang = tk.Button(win, image=img_kaoliang, command=select_kaoliang)
    btn_soju = tk.Button(win, image=img_soju, command=select_soju)
    btn_random = tk.Button(win, image=img_random, command=select_random)
    btn_payment = tk.Button(win, text='결제', command=select_pay)

    btn_prev = ttk.Button(win, text='<==이전', command=click_prev)
    btn_next = ttk.Button(win, text='다음==>', command=click_next)

    btn_close = ttk.Button(win, text='프로그램 종료', command=finish)
    # -----------------------------------


    # Label
    # -----------------------------------
    lbl_select_payment = tk.Label(win, text='결제 방식 : ')
    lbl_total = tk.Label(win, text='')
    lbl_foods = tk.Label(win, text='안주 미리보기')
    lbl_foods_img1 = tk.Label(win, image=foods_list[0])
    lbl_foods_img2 = tk.Label(win, image=foods_list[1])
    # -----------------------------------


    # RadioButton
    # -----------------------------------
    selected_payment = tk.IntVar()
    rdo_cash = tk.Radiobutton(win, text='현금', variable=selected_payment, value=0)
    rdo_card = tk.Radiobutton(win, text='카드', variable=selected_payment, value=1)
    # -----------------------------------


    # grid
    # -----------------------------------
    btn_beer.grid(row=0, column=0)
    btn_wine.grid(row=0, column=1)
    btn_kaoliang.grid(row=0, column=2)
    btn_soju.grid(row=0, column=3)
    btn_random.grid(row=0, column=4)
    lbl_total.grid(row=1, column=0, columnspan=5, sticky=tk.EW)
    lbl_select_payment.grid(row=2, column=0, columnspan=2)
    rdo_cash.grid(row=2, column=2)
    rdo_card.grid(row=2, column=3)
    btn_payment.grid(row=3, column=0, columnspan=5, pady=20)
    lbl_foods.grid(row=4, column=0, columnspan=5)
    btn_prev.grid(row=5, column=0, sticky=tk.E)
    lbl_foods_img1.grid(row=5, column=1, columnspan=2)
    lbl_foods_img2.grid(row=5, column=2, columnspan=2)
    btn_next.grid(row=5, column=4, sticky=tk.W)
    btn_close.grid(row=6, column=4, sticky=tk.E)
    # -----------------------------------


    # Binding
    # -----------------------------------
    # win.bind('a', pg_dw)
    # win.bind('d', pg_up)
    win.bind('<KeyPress>', key_down)
    # -----------------------------------

    # 로그에 날짜, 시간 입력
    # -----------------------------------
    fp = open('./text/bill.txt', 'a')
    print('\n', '='*20, file=fp)
    print(str(dt.datetime.now())[:19], file=fp)
    # -----------------------------------

    # mainloop
    win.mainloop()

    # 파일입출력 닫기
    fp.close()