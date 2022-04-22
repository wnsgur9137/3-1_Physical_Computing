# 조건문 cont.

# age = int(input('나이는? '))
#
# if 0 <= age < 8 :
#     print('어린이 요금은 5000원 입니다.')
# elif 8 <= age < 19 :
#     print('청소년 요금은 9000원 입니다.')
# elif age >= 19 :
#     print('성인 요금은 11000원 입니다.')
# else :
#     print('정확한 나이를 입력해 주세요')


# age = int(input('나이는? '))
# price = 0
#
# if 0 <= age < 8 :
#     price = 5000
# elif 8 <= age < 19 :
#     price = 9000
# elif age >= 19 :
#     price = 11000
# else :
#     print('정확한 나이를 입력해주세요')
#
# print('요금은 ' + str(price) + '원 입니다.')


# options = ['콜라', '치즈토핑', '버섯', '치즈크러스터']
# if '버섯' in options :
#     print('버섯을 추가합니다.')
# if '페퍼로니' in options :
#     print('페퍼로니를 추가합니다.')
# if '치즈토핑' in options :
#     print('치즈토핑을 추가합니다.')
#
# print('\n피자 주문이 완료 됐습니다.')

# 반복문
for i in range(5) : # i값이 0부터 시작해서 5 전까지
    print(i, end=' ')
print()

for i in range(2, 5) : # 2은 시작 값, 5는 끝 값 + 1
    print(i, end=' ')
print()

for i in range(1, 6, 2) : # 2는 시작 값, 5는 끝 값 + 1, 증감 step
    print(i, end=' ')