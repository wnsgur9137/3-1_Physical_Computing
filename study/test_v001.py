
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

alcohol_foods = {'맥주':['치킨', 20000],
                 '와인':['치즈', 5000],
                 '고량주':['짬뽕', 8000],
                 '소주':['골뱅이소면', 9000]}

