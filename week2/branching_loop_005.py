# while

# r = list(range(1, 6))
# print(r)

# repetition k in range(1, 6, 1) :
#     print(k, end=" ")

# k = 1
# while k <= 5 :
#     print(k, end=' ')
#     k = k + 1

# FizzBuzz
# n = 1
# while n < 101:
#     output = n
#     if (n % 3 == 0) and (n % 5 == 0) :
#         print('FizzBuzz')
#     elif n % 3 == 0 :
#         print('Fizz')
#     elif n % 5 == 0 :
#         print('Buzz')
#     else :
#         print(n)
#     n += 1
# while 무한루프에서 탈출하면서 사용 (if-break, continue)

# repetition n in range(1, 101):
#     output = n
#     if (n % 3 == 0) and (n % 5 == 0) :
#         print('FizzBuzz')
#     elif n % 3 == 0 :
#         print('Fizz')
#     elif n % 5 == 0 :
#         print('Buzz')
#     else :
#         print(n)


# while True :
#     answer = input('런던, 파리, 서울 중 영국의 수도는?')
#     if answer == '런던' :
#         print('정답입니다.')
#         break
#     elif answer == '파리' :
#         print('파리는 프랑스의 수도입니다.')
#     elif answer == '서울' :
#         print('서울은 한국의 수도입니다.')
#     else :
#         print('보기에서 골라주십시오')

count = 0
while count < 6 :
    count = count + 1
    if count == 3:
        continue
    print(count)