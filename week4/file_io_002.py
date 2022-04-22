#file io (cont.)

# 안주 추천 프로그램 v0.5
import random
alcohol_foods = {}

with open('alcohols.txt', 'r') as fp1:
    with open('foods.txt', 'r') as fp2:
        alcohols = fp1.readlines() # 리스트 변수 alcohols
        foods = fp2.readlines() # 리스트 변수 foods
        for k in range(len(alcohols)):
            alcohol_foods[alcohols[k].strip('\n')] = foods[k].strip('\n')
print(alcohols)
print(foods)
print(alcohol_foods)

while True:
    alchol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
    if alchol == '결제':
        break
    if alchol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
    elif alchol == '아무거나':
        any = random.choice(list(alcohol_foods))
        print('{0}을 추천합니다. 어울리는 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
    else :
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요'.format(alchol))
