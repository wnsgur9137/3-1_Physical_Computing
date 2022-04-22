# -*- coding: utf-8 -*-

# 리스트 002

# 리스트 원소 삭제 (계속)
subjects = ['english', 'python', 'java']
print(subjects)
print(subjects.remove('python')) # remove는 리턴하지 않기때문에 None이 출력된다.
print(subjects)

subjects.insert(2, 'python')

print(subjects.pop()) # pop 함수는 삭제하려는 원소 값을 리턴 후 삭제
print(subjects)

# 리스트의 위치 출력
print(subjects.index('java')) # java의 index(주소)

# 리스트 원소의 값 세기
subjects.append('java')
subjects.append('java')
print(subjects)
print(subjects.count('java')) # 'java' 원소의 수
print(subjects.count('english')) # 'english' 원소의 수

# in 키워드
print('python' in subjects) # 존재 여부에 따라 Flase, True를 반환
print('java' in subjects)

# 리스트 원소의 개수 반환
subjects.insert(0, 'python')
print(len(subjects))
print(subjects)

# 리스트를 문자열로 변환하는 join 함수
subjects_string = '/'.join(subjects)
print(subjects_string)

# 문자열을 리스트로 변환하는 split 함수
subjects_lists = subjects_string.split()
print(subjects_lists)
print(len(subjects_lists))

subjects_lists = subjects_string.split('j')
print(subjects_lists)

subjects_lists = subjects_string.split('/')
print(subjects_lists)

# 리스트 원소 정렬
# subjects.sort() # 오름차순 정렬 (사전순)
subjects.sort(reverse=True) # 내림차순 정렬 (사전순)
print(subjects)

# sort는 원본의 값을 바꿔버린다.
# sorted는 원본의 값을 그대로 유지한다.
list_a = [2, 3, 1]
list_copy = sorted(list_a)
print(list_a)
print(list_copy)

# 숫자와 문자는 비교할 수 없다.
list_a.insert(1, 3.1)
list_a.append('python')
print(list_a)