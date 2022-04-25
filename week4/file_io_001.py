# file io

# 파일 객체 = open(파일 경로, 읽기 모드)
# w : 쓰기모드, r : 읽기모드, a : 이어쓰기 모드
# 파일을 닫을  파일객체.close()

# 파일 쓰기
fp = open('war_flower.txt', 'w')
print('고니', file=fp) # 실제 쓰기
print('정마담', file=fp)
print('아귀', file=fp)
fp.write('너부리')
fp.close()

# 파일 읽기 (아무것도 입력하지 않을 시 읽기모드)
fp = open('war_flower.txt', 'r')
lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
# print(lines)
for line in lines:
    # print(line.rstrip('\n'))
    # print(line.strip('\n'))
    print(line[0:-1])
# repetition line in fp:
#     print(line, end='')

# with as 구문을 사용하면 파일을 열고 해당 구문이 끝나면 자동으로 닫히게 된다.
with open('war_flower.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        print(line[:-1])