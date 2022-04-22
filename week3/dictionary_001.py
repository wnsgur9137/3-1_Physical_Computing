# dictionary

# 리스트와 비슷하나 순서를 따지지 않는다.
# 리스트는 , 와 []를 이용해 원소를 나열하였는데, 딕셔너리는 {}를 사용한다.
# key : value 형태로 들어가게 된다.
# key 값은 중복이 될 수 없다.

# #           key  : value
# fruits = {'apple':'사과',
#           'watermelon':'수박'}
#
# print(fruits['apple'])
# print(fruits['watermelon'])
# print("print(fruits) : ", end=" ")
# print(fruits)
#
# # 삽입
# fruits['kiwi'] = 'kiwi'
# print(fruits)
#
# # 수정
# fruits['kiwi'] = '키위'
# print(fruits)
#
# empty = {}
# print(type(fruits), type(empty))

# # 이중 리스트
# test = [['python', 3], ['english', 2], ['dance', 1]]
# print(test)
# print(test[1])
# print(test[1][0])
#
# print('\n', '-' * 50, '\n')
#
# # 딕셔너리
# print(test)
# print(dict(test))
#

# # dict() - 딕셔너리 변환 함수
# test1 = [['python', 3], ['english', 2], ['dance', 1]]
# print(test1[1][0])
# print(test1)
# print(dict(test1))
#
# test2 = ['ab', 'cd', 'ef']
# print(test2[1][0])
# print(test2)
# print(dict(test2))

# update() - 결합
fruits = {'apple':'사과', 'watermelon':'수박'}
fruits['banana'] = '바나나'
print(fruits)

others = {'strawberry':'딸기', 'kiwi':'키위', 'banana':'버내너'}
fruits.update(others) # 중복된 키가 있을 경우 수정
print(fruits)

# del - 삭제
del fruits['apple']
print(fruits)

# clear() - 전체 원소 삭제
fruits.clear()
print(fruits)

# del - 딕셔너리 삭제
del fruits
print(fruits) # error