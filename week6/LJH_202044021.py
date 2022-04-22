import tkinter as tk # GUI 작업을 위함
import random # 메뉴 중 '아무거나'를 선택할 시 랜덤으로 선택하기 위함
import datetime # 프로그램 실행 시 txt파일에 날짜를 기록하기 위함

# alcohol_foods 딕셔너리
alcohol_foods = {'맥주':['치킨', 20000],
                 '와인':['치즈', 5000],
                 '고량주':['짬뽕', 8000],
                 '소주':['골뱅이소면', 9000]}

def select_alcohol(): # 버튼을 클릭할 시 실행될 함수
    try :
        # 문자열로 입력받는다. (en_input에 입력한 문자열을 가져옴)
        choice_alcohol = str(en_input.get()).strip()

        if choice_alcohol == '': # 아무것도 입력하지 않았을 시
            # 로그에 남기지 않고 공백을 입력하지 말라는 경고메세지 출력
            lbl_result.configure(text="메뉴를 입력해주세요.")

        elif choice_alcohol == '결제': # '결제' 입력시
            # print('감사합니다. 다음에 또 방문 부탁드려요~') # 콘솔 출력(확인용)
            lbl_result.configure(text='감사합니다. 다음에 또 방문 부탁드려요~') # lbl_result에 출력
            print('감사합니다. 다음에 또 방문 부탁드려요~', file=fp) # 파일 이어쓰기

        elif choice_alcohol in alcohol_foods.keys(): # 'alcohol_foods'의 키값에 해당하는 메뉴를 선택시
            # print('{0} 입력 : {0}에 어울리는 안주는 {1}입니다. 안주가격은 {2}원'.format(choice_alcohol, alcohol_foods[choice_alcohol][0], alcohol_foods[choice_alcohol][1])) # 콘솔 출력(확인용)
            lbl_result.configure(text='{0} 입력 : {0}에 어울리는 안주는 {1}입니다. 안주가격은 {2}원'.format(choice_alcohol, alcohol_foods[choice_alcohol][0], alcohol_foods[choice_alcohol][1])) # lbl_result에 출력
            print('{0} 입력 : {0}에 어울리는 안주는 {1}입니다. 안주가격은 {2}원'.format(choice_alcohol, alcohol_foods[choice_alcohol][0], alcohol_foods[choice_alcohol][1]), file=fp) # 파일 이어쓰기

        elif choice_alcohol == '아무거나': # '아무거나' 입력시
            alcohol_foods_list = list(alcohol_foods) # 'alcohol_foods' 딕셔너리의 키값(주류)으로 리스트 생성
            any = random.choice(alcohol_foods_list) # 'alcohol_foods'의 키값(주류) 중 랜덤으로 선택

            # print('아무거나 입력 : {0}을 추천합니다. 안주는 {1}~~ 안주가격은 {2}'.format(any, alcohol_foods[any][0], alcohol_foods[any][1])) # 콘솔 출력(확인용)
            lbl_result.configure(text='아무거나 입력 : {0}을 추천합니다. 안주는 {1}~~ 안주가격은 {2}원'.format(any, alcohol_foods[any][0], alcohol_foods[any][1])) # lbl_result에 출력
            print('아무거나 입력 : {0}을 추천합니다. 안주는 {1}~~ 안주가격은 {2}'.format(any, alcohol_foods[any][0], alcohol_foods[any][1]), file=fp) # 파일 이어쓰기

        else :
            # print('{0} 입력 : {0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(choice_alcohol)) # 콘솔 출력(확인용)
            lbl_result.configure(text='{0} 입력 : {0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(choice_alcohol)) # lbl_result에 출력
            print('{0} 입력 : {0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(choice_alcohol), file=fp)

    except: # try문에서 에러가 발생할 시 처리한다.
        print('에러 발생') # 콘솔에 '에러 발생' 출력
    finally: # 오류가 발생 여부 상관없이 실행(en_input 엔터티 공백으로 만듦)
        en_input.delete(0, 'end')



# 프로그램 실행 시 로그 파일에 남길 시간
# -------------------------
fp = open('bill.txt', 'a') # 파일을 불러온다.
# print(str(datetime.datetime.now())[:19]) # 콘솔 출력(확인용)
print('\n', '=' * 20, file=fp) # 구분선
print(str(datetime.datetime.now())[:19], file=fp) # 파일 이어쓰기(현재 시간을 년도-월-일 시간:분:초로 입력한다.)
fp.close() # 'bill.txt' 파일을 닫는다.
# -------------------------


# GUI
# -------------------------
win = tk.Tk()
win.title('3학년 A반 202044021 이준혁') # 프로그램 타이틀
win.geometry('400x150') # 사이즈

lbl_title = tk.Label(win, text="주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?") # 메뉴 보기 레이블
lbl_result = tk.Label(win, text="3학년 A반 202044021 이준혁") # 추천된 결과가 출력되는 레이블
en_input = tk.Entry(win) # 입력받는 엔터티
btn_select = tk.Button(win, text='확인', command=select_alcohol) # '확인' 버튼

# pack()
# -------------------------
lbl_title.pack()
lbl_result.pack()
en_input.pack()
btn_select.pack()
# -------------------------

# 프로그램 실행시 자동으로 en_input 엔터티를 선택
en_input.focus()

# 로그를 저장할 파일을 '이어쓰기'모드로 불러온다.
fp = open('bill.txt', 'a')

# GUI mainloop()
win.mainloop()

# 사용한 파일 닫기 (bill.txt)
fp.close()