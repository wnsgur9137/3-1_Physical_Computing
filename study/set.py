# set() -> new empty set object
# set(iterable) -> new set object

# set() 키워드 혹은 중괄호 이용
# 순서가 없음
# 고유한 값을 가짐 (값 중복 불가능)
# mutable(=값이 변하는) 객체

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

# 교집합 메서드 inertsection
print(s1.intersection(s2))
# 교집합 연산자
print(s1 & s2)

# 합집합 메서드 union
print(s1.union(s2))
# 합집합 연산자 |
print(s1 | s2)

# 차집합 메서드 difference
print(s1.difference(s2))
print(s2.difference(s1))
# 차집합 연산자 -
print(s1 - s2)
print(s2 - s1)

# 집합이 같은지
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
s3 = {1, 2, 3, 4, 5}
if s1 == s2:
    print('s1 and s2 are the same')
else:
    print('s1 and s2 are not the same')

if s1 == s3:
    print('s1 and s3 are the same')
else:
    print('s1 and s3 are not the same')

# 집합이 아예 다른지
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
s3 = {1, 2, 3, 4, 5}
s4 = {6, 7, 8, 9, 10}

if s1.isdisjoint(s2):
    print('s1 and s2 are not the same  ')