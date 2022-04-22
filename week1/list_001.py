# -*- coding: utf-8 -*-

# 리스트
# 리스트는 특성 순서가 있는 항목의 모음
# 대괄호 [ ] 쉼표 , 기호를 사용

# print(type(empty_lists))
# print(type(5))
# print(type(5.7))
# print(type('python'))

# list 생성
# empty_lists = [] # list 만드는 방법 1
empty_lists = list() # list 만드는 방법 2
subjects = ['english', 'python', 'java']
print(type(empty_lists))
print(type(subjects))
print(empty_lists)
print(subjects)

# list 인덱싱
print(subjects[1])
print(subjects[-2])

# 리스트 삽입
# append(추가), insert(삽입)

subjects.append('C++')
print(subjects)
print(subjects[1])
print(subjects[-2])

subjects.insert(2, 'math')
print(subjects)

# 리스트 원소 수정
subjects[3] = 'assembly'
print(subjects)

# 리스트 원소 삭제
# del subjects[-1]
# del subjects[4]
subjects.pop() # 맨 뒤의 원소를 삭제한다.
print(subjects)
subjects.append('math')
subjects.remove('math') # 중복일 경우 맨 앞의 원소를 삭제한다.
print(subjects)

subjects.remove(subjects[1])
print(subjects)