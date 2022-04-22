# 함수 (Function cont.)
#
# # factorial
# # 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# def factorial_recursion(number) :
#     """
#     팩토리얼 함수
#     재귀 함수 사용
#     f(n) = n * (n-1) * (n-2) * (n-3) ... * 1
#     f(5) = 5 * (5-1) * (5-2) * (5-3) ... * 1
#     f(5) = 5 * f(n-1)
#     """
#     if number == 0 :
#         return 1
#     else :
#         return number * factorial_recursion(number-1)
#
# def factorial_loop(number) :
#     """
#     팩토리얼 함수
#     반복문 사용
#     """
#     result = 1
#     for i in range(1, number+1) :
#         result = result * i
#         # print(result, ' * ', i, ' = ', result)
#
#     return result
#
# # print(factorial_loop(int(input())))
# # print(factorial_recursion(int(input())))
#
# print(factorial_recursion(4))
# print(factorial_recursion(6))
# print(factorial_loop(6))
# print(factorial_loop(4))

# # fibonacci
# # 피보나치 수열은 성능 상의 문제가 있다.
# # 재귀호출이 빈번히 일어날수록 속도가 느려진다
# def fibo_recursion(number) :
#     """
#     f(n) = f(n-1) + f(n-2)
#     f(0) = 0
#     f(1) = 1
#     f(2) = 1
#     f(3) = f(2) + f(1)
#          = 1 + 1
#     f(4) = f(3) + f(2)
#          = 2 + 1
#     """
#
#     if number == 1 :
#         return 1
#     if number == 2 :
#         return 1
#     else :
#         return fibo_recursion(number-1) + fibo_recursion(number-2)
#
# for k in range(1, 8) :
#     print('피보나치 {0} : {1}'.format(k, fibo_recursion(k)))

# 함수의 매개변수로 함수 전달하기
# def print_hi(hi) :
#     for k in range(5) :
#         hi()
#
# def hi() :
#     print('hello')
#
# hi()
# print_hi(hi)
#
# # map(함수, 순환가능한 자료구조)
# # list, dictionary, string, range
# def square(number) :
#     return number * number
#
# # for k in range(1, 6) :
# #     print(square(k))
# # print(list(map(square, [1, 2, 3, 4, 5])))
#
# result = []
# for k in range(1, 6) :
#     result.append(square(k))
# print(result)
#
def square(number) :
    return number * number
def odd(number) :
    return number % 2 == 1

print(list(map(square, [1, 2, 3, 4, 5])))

# filter(함수, 순환가능한 자료구조)
# return 값과 비교하여 True일 때만 출력
print(list(filter(odd, [1, 2, 3, 4, 5])))

# 람다함수, 제너레이터