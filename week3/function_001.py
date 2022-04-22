# 함수 (Function)
# 한 가지 작업을 수행하도록 디자인된 코드블럭 or 코드의 집합

# # 함수의 시작 def
# def test(name) :
#     print('hi ' + name)
#     return '이름을 출력함'
#
# name = test(input()) # 함수의 호출 (Function call)
#
# print("return : " + name)

# def minus(a, b) :
#     """
#     두 수의 차를 구하는 함수
#     매개변수는 a와 b로 받음
#     """
#     return a - b
#
# print(minus(3, 1))
# # print(minus(3))        # type error
# # print(minus(3, 1, 99)) # type error
# # help(minus)
# # print(minus.__doc__)

# 가변 매개변수
# 가변 매개변수를 사용할 경우 다른 변수를 선언할 수 없다.
def print_even(times, *values) :
    for value in values :
        print(times * value)
print_even(2, -9, 11, 7, 100, 6)

# default parameter(기본 매개변수)는 맨 뒤에 위치해야 한다.
# def print_even(times=3, value) : # error
def print_even2(value, times=3) :
    print(times * value)

print_even2(12)