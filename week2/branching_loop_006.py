# list comprehersion

# numbers = []
# for k in range(0, 10, 2) :
#     numbers.append(k * k)
# print(numbers)

# 리스트이름 = [ 표현식 for 반복할 변수명 in 수(range함수 또는 리스트 등)]
# numbers = [k * k for k in range(0, 10, 2)]
# print(numbers)

# # 시네마 키오스크 v0.3
# # ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = int(input('몇 분이 오셨죠? '))
# ages = [int(input('나이는? ')) for i in range(humans)]
# # for i in range(humans):
# #     ages.append(int(input('나이는? ')))
#
# for age in ages:
#     if 0 <= age < 8:
#         price += 5000
#         kids += 1
#     elif 8 <= age < 19:
#         price += 9000
#         mids += 1
#     elif age >= 19:
#         price += 11000
#         adults += 1
#     else:
#         print('정확한 나이를 입력해주세요')
#
# print('=' * 50)
# print('어린이 : {0}\t청소년 : {1}\t성인 : {2}'.format(kids, mids, adults))
# print('총 인원 : {0}'.format(humans))
# print('총 금액 : {0}원'.format(price))
# print('=' * 50)

numbers = [k*k for k in range(0, 10, 2)]
print(numbers)
# [0, 4, 16, 36, 64]

n = [x for x in range(1, 11) if x % 3 == 0]
print(n)
# [3, 6, 9]

n = []
for x in range(1, 11):
    if x % 3 == 0:
        n.append(x)