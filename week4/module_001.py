# module

# built in module 내장(표준)모듈
# import math
from math import ceil, floor, sqrt
import random

# print(math.ceil(3.1))
# print(math.floor(4.9))
# print(math.sqrt(16))
print(ceil(3.1))
print(floor(4.9))
print(sqrt(16))
print(random.randint(1, 6))

# 사용자 정의 모듈
# 1
# import my_math
#
# print(my_math.factorial_loop(5))
# print(my_math.square(5))
# print(my_math.fibo_recursion(5))
# print(my_math.power(2, 10))

# 2
# from 모듈이름 import 가져오고 싶은 함수 또는 변수
# 모듈 이름을 생략하고 함수를 사용한다.
# from my_math import factorial_loop, square, fibo_recursion, power
#
# print(factorial_loop(5))
# print(square(5))
# print(fibo_recursion(5))
# print(power(2, 10))

# 3
# import my_math as mm
#
# print(mm.factorial_loop(5))
# print(mm.square(5))
# print(mm.fibo_recursion(5))
# print(mm.power(2, 10))