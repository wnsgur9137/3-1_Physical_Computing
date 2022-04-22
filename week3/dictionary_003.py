# # 음식 추천 프로그램 v0.3
# # import random
# # star = ['테란', '저그', '프로토스']
# # print(random.choice(star))
# import random
#
# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# print(list(alcohol_foods))
#
# while True:
#     alcohol = input('주문하실 술은? (맥주/와인/고량주/소주/아무거나/결제) : ')
#     if alcohol == '결제' :
#         break
#     if alcohol in alcohol_foods.keys() :
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     elif alcohol == '아무거나' :
#         print(random.choice(list(alcohol_foods)))
#     else :
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주십시오.'.format(alcohol))

# alcohol_foods = {'맥주':'치킨',
#                  '와인':'치즈',
#                  '고량주':'짬뽕',
#                  '소주':'골뱅이소면'}
#
# # copy() - 같은 메모리 주소 참조
# # copy_alcohol = alcohol_foods
# # copy_alcohol['소주'] = '두부김치'
# # print(copy_alcohol)
# # print(alcohol_foods)
#
# copy_alcohol2 = alcohol_foods.copy()
# copy_alcohol2['소주'] = '두부김치'
# print(copy_alcohol2)
# print(alcohol_foods)

# tuple
# 리스트와 비슷하다. (같은 순서를 가진다.)
# immutable = 불변
# 튜플의 원소를 정의한 후에는 추가, 삭제, 수정 불가
# 상수의 리스트라고 할 수 있다.
# list = [], dictionary = {}, tuple = ()


# # empty = ()
# # numbers = (1, -9, 7)
# # print(type(empty))
# # print(numbers)
# # print(numbers[1])
# # print(numbers[-1])
# # numbers[0] = 5 # 튜플인 아이템 할당 기능을 제공하지 않는다. (불변)
#
# subjects = ('python', 'c++', 'english') # packing
# # for subject in subjects :
# #     print(subject)
# kim, han, tom = subjects # unpacking
# print(kim, tom, han)

a = input()
b = input()
# t = b
# b = a
# a = t
a, b = b, a # packing과 unpacking을 동시에 수행
print(a, b)