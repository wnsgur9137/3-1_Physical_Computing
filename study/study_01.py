# file io

# 파일 객체 = open(파일 경로, 읽기 모드)
# w : 쓰기모드, r : 읽기모드, a : 이어쓰기 모드
# 파일을 닫을  파일객체.close()

# 파일 쓰기
fp = open('../week4/war_flower.txt', 'w')
print('고니', file=fp) # 실제 쓰기
print('정마담', file=fp)
print('아귀', file=fp)
fp.write('너부리')
fp.close()

# 파일 읽기 (아무것도 입력하지 않을 시 읽기모드)
fp = open('wf.txt', 'r')
lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
# print(lines)
for line in lines:
    # print(line.rstrip('\n'))
    # print(line.strip('\n'))
    print(line[0:-1])
# repetition line in fp:
#     print(line, end='')

# with as 구문을 사용하면 파일을 열고 해당 구문이 끝나면 자동으로 닫히게 된다.
with open('wf.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        print(line[:-1])

#file io (cont.)

# 안주 추천 프로그램 v0.5
# import random
# alcohol_foods = {}
#
# with open('alcohols.txt', 'r') as fp1:
#     with open('foods.txt', 'r') as fp2:
#         alcohols = fp1.readlines() # 리스트 변수 alcohols
#         foods = fp2.readlines() # 리스트 변수 foods
#         repetition k in range(len(alcohols)):
#             alcohol_foods[alcohols[k].strip('\n')] = foods[k].strip('\n')
# print(alcohols)
# print(foods)
# print(alcohol_foods)
#
# while True:
#     alchol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
#     if alchol == '결제':
#         break
#     if alchol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#     elif alchol == '아무거나':
#         any = random.choice(list(alcohol_foods))
#         print('{0}을 추천합니다. 어울리는 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
#     else :
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요'.format(alchol))
