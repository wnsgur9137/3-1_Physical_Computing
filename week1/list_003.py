# -*- coding: utf-8 -*-

# 리스트 003

my_utube = ['악뮤', '볼사', '코노', '언더독', '홍수웅', '빅뱅']
ur_utube = my_utube[0:5] # 5번 앞까지 자른다.

print(ur_utube)
del my_utube[-1]
print(my_utube)

my_utube.append('태양')
print(my_utube)

a = [2, 3, 1, 5]
# b = a # 공유
# b = a[0:] # 슬라이싱을 하게 되면 공유하지 않는다.
# b = a.copy() # copy 함수를 사용하면 공유하지 않는다.
b = list(a) # list 함수 또한 공유하지 않는다.
print(b)
b[-2] = 4
print(b)
print(a)
print(id(a), id(b))

my_utube = ['악뮤', '볼사', '코노', '언더독', '홍수웅', '태양']
ur_friends = ['릴러말즈', '슈퍼비']
# friends = my_utube[2:5]
# friends = my_utube[-4:-1]
# friends = my_utube[2:-1]
# friends = my_utube[-4:5]
friends = my_utube[2:len(my_utube)-1]
print(friends)

friends.extend(ur_friends)
print(friends)