# -*- coding: utf-8 -*-

# 자료형 (cont.)
# 문자열 함수

# words = 'Life is too short, \n You need\t Python'
# # temp = words.title() # 각 단어의 첫 글자를 대문자로
# # temp = words.lower() # 모두 소문자로
# temp = words.upper()   # 모두 대문자로
#
# print(temp)

# # strip()
# trim1 = 'python'
# trim2 = '  python   '
# trim3 = '&& &python& &'
#
# print("1:", trim1 + "\n" + trim2)
# print("2:",trim1 + "\n" + trim2.strip())
# print("3:", trim3.strip('&'))
# print("4:", trim3.lstrip('&'))
# print("5:",trim3.rstrip('&'))
#
# print(trim1, end='')
# print(trim2.strip('&'))

# # str()
# print('1' + "hi")
# print(str(1) + "hi")

# # int()
# a = '1'
# b = 2
# print(int(a) + b)

# input()
print("input name")
name = input()
print(name)