# PhotoViewer v0.1
import datetime as dt           # 날짜
import tkinter as tk            # GUI
from tkinter import ttk         # 디자인
from tkinter import messagebox  # 안내 메세지


def click_next():   # 다음 버튼
    # idx = idx + 1 # ERROR (idx가 전역변수인지, 지역변수인지 모르기 때문) -> global을 사용해야한다.
    global idx  # 전역변수를 사용하기 위함
    idx = idx + 1   # idx는 리스트의 인덱스를 지정하기 위해, 페이지 출력을 위해 사용
    if idx > len(photos)-1: # 리스트의 인덱스보다 클경우
        idx = 0 # 리스트의 첫 번째 인덱스로 지정
    p = tk.PhotoImage(file=photos[idx]) # 경로 지정
    lbl_page.configure(text=f'{idx+1}/{len(photos)}')   # 페이지 출력
    lbl_photo.configure(image=p)       # 준비
    lbl_photo.image = p # 이미지를 출력


def click_prev():   # 이전 버튼
    global idx
    idx = idx - 1
    if idx < 0: # 0보다 작을 경우
        idx = len(photos) - 1   # 마지막 인덱스로 이동
    p = tk.PhotoImage(file=photos[idx])  # 경로 지정
    lbl_page.configure(text=f'{idx + 1}/{len(photos)}') # 페이지 출력
    lbl_photo.configure(image=p)  # 준비
    lbl_photo.image = p # 이미지 출력


def pg_dw(ev):  # 키 입력할 경우(<Next>, right)
    click_next()


def pg_up(ev):  # 키 입력할 경우(<Prior>, left)
    click_prev()


def click_photo(ev):
    messagebox.showinfo('좌표', f'({ev.x}, {ev.y})')


# 전역변수
photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']  # 이미지 경로를 저장
idx = 0 # 리스트 인덱스 지정, 페이지 출력을 위해 사용
date_now = str(dt.datetime.now())[:19] # 현재 시간을 년도-월-일 시간:분:초로 입력한다. (프로그램 실행 시간)

# 윈도우 설정
w = tk.Tk() # 윈도우 생성
w.title('PhotoViewer v0.1') # 윈도우 타이틀
w.geometry('600x600')   # 윈도우 크기

# 레이블/버튼 생성
p = tk.PhotoImage(file='michael.PNG')   # 초기 이미지 경로 설정
lbl_photo = ttk.Label(w, image=p)   # 이미지를 출력할 레이블
lbl_page = ttk.Label(w, text=f'{idx+1}/{len(photos)}')  # 페이지를 출력할 레이블
btn_next = ttk.Button(w, text='다음 ==>', command=click_next) # 다음 버튼 (click_next 함수 실행)
btn_prev = ttk.Button(w, text='<== 이전', command=click_prev) # 이전 버튼 (click_next 함수 실행)0
lbl_date = ttk.Label(text=f'{date_now}') # 프로그램 실행 시간을 출력할 레이블

# 바인딩
w.bind('<Next>', pg_dw) #PgDn 버튼을 클릭할 시, pg_dw 함수 실행
w.bind('right', pg_dw)  #오른쪽 방향키를 클릭할 시, pg_dw 함수 실행
w.bind('<Prior>', pg_up)#PgUp 버튼을 클릭할 시, pg_up 함수 실행
w.bind('left', pg_up)   #왼쪽 방향키를 클릭할 시, pg_up 함수 실행
# 마우스 왼클릭 할 시 click_photo 함수 실행
# <Button> -> 마우스의 모든 클릭
# <Button-1> -> 마우스 좌클릭
# <Button-2> -> 마우스 휠클릭
# <Button-3> -> 마우스 우클릭
lbl_photo.bind('<Button-1>', click_photo)

# 위치를 쉽게 지정하기 위해 그리드(행, 열)로 집어넣는다.
# sticky -> 안드로이드 스튜디오의 match_parent
lbl_photo.grid(row=0, column=0, columnspan=3)   # 0번째 행, 0번째 열, 열병합 3
btn_prev.grid(row=1, column=0, sticky=tk.EW)    # 1번째 행, 0번째 열
lbl_page.grid(row=1, column=1)                  # 1번째 행, 1번째 열 (페이지 출력)
btn_next.grid(row=1, column=2, sticky=tk.EW)    # 1번째 행, 2번째 열
lbl_date.grid(row=2, column=0, columnspan=3)    # 2번째 행, 0번째 열, 열병합 3

w.mainloop()