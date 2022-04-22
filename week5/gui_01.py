# # 안주 추천 프로그램 v0.7
#
# import random
# alcohol_foods = {}
# a = input('술의 종류를 보관하고 있는 파일? ')
# f = input('안주의 종류를 보관하고 있는 파일? ')
#
# try:
#     with open(a, 'r') as fp1:
#         with open(f, 'r') as fp2:
#             alcohols = fp1.readlines()  # 리스트 변수 alcohols
#             foods = fp2.readlines()  # 리스트 변수 foods
#             for k in range(len(alcohols)):
#                 alcohol_foods[alcohols[k].strip('\n')] = foods[k].strip('\n')
# except FileNotFoundError as e:
#     print('파일이 없거나 경로가 틀렸습니다. : {0}'.format(e))
# else:
#     while True:
#         alcohol = input('주문하실 술(' + '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) + '/아무거나/결제)은? ')
#         if alcohol == '결제' or alcohol == 'exit':
#             break
#         if alcohol in alcohol_foods.keys():
#             print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#         elif alcohol == '아무거나':
#             any = random.choice(list(alcohol_foods))
#             print('{0}을 추천합니다. 어울리는 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
#         else:
#             print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요'.format(alcohol))
# finally:
#     print('프로그램 종료')



# graphic user interface

# import tkinter as tk
#
# win = tk.Tk() # 윈도우 객체 생성
# win.title('GUI') # 제목 표시줄
# win.geometry('600x150') # 가로 세로 크기 지정
# win.resizable(width=True, height=False) # 너비 높이 고정
#
# win.mainloop()


# 레이블 실습
from tkinter import *

w = Tk() # 윈도우 객체 생성
w.title('레이블 실습') # 제목 표시줄

lbl_1 = Label(w, text='python programming')
lbl_2 = Label(w, text='study 공부', font=("돋움체", 20), fg="red")
lbl_3 = Label(w, text='test', fg='blue', bg='green', width=20, height=10, anchor=SE)

lbl_1.pack()
lbl_2.pack()
lbl_3.pack()

w.mainloop()