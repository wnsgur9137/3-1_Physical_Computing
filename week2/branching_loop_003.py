# 반복문 cont.
# for 변수 in range(변수 시작값, 끝값, 증감값):

# for n in range(11):
#     print(n)
#
# for n in range(5, 11):
#     print(n)

# 짝수 출력
# for n in range(2, 11, 2):
#     print(n)

# for n in range(1, 11):
#     if n % 2 == 0:
#         print(n)

# for n in range(1, 11):
#     if (n % 2) != 0:
#         continue
#     print(n)

# # step에 감소식
# for n in range(10, 0, -1):
#     print(n)

# 문자열 문자 출력
# words = 'I love python'
# for word in words:
#     print(word)

# 리스트 원소 출력
# words = ['I', 'love', 'python']
# for word in words:
#     print(word)

# for i in range(0, 3, 1):
# for i in range(3): # 인덱스 값을 활용 (선택 구간 유리)
#     print(words[i])
# for i in range(5): # index out of range 에러
#     print(words[i])

# words = 'I love python'
# for word in words:
#     print(word, end='')
# print()
# for i in range(5):
#     print(words[i], end='')
# print()
# for i in range(len(words)):
#     print(words[i], end='')

ages = []
price = 0
humans = int(input('몇 분이 오셨죠? '))
for i in range(humans):
    ages.append(int(input('나이는? ')))

for age in ages:
    if 0 <= age < 8:
        price += 5000
    elif 8 <= age < 19:
        price += 9000
    elif age >= 19:
        price += 11000
    else:
        print('정확한 나이를 입력해주세요')

print('총 금액은 ' + str(price) + '원 입니다.')