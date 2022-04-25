# exception handling

# 실행전 에러 - syntax(구문 에러)
# 예시
# repetition k in range(5):
# print(k)

# a = input()
# b = input()
# if a.isdigit() and b.isdigit(): # 숫자로만 구성되어 있는가 (-99와 같은 기호를 추가할 시 False)
#     print(int(a)+int(b))
# else:
#     print('입력된 수는 정수가 아닙니다.')


# try:
#   예외가 발생할 가능성이 있는 코드
# except:
#   예외가 발생했을 때 실행할 코드
# else:
#   예외가 발생하지 않았을 때 실행할 코드
# finally:
#   무조건 실행
try:
    c = list()
    c.append('사과')
    a = int(input())
    b = int(input())
    print(a / b)
    print(c[0])
except IndexError:
    print('리스트의 범위를 벗어난 인덱스가 사용되었습니다.')
except ZeroDivisionError:
    print('분모에 0이 올 수 없습니다.')
except ValueError:
    print('입력된 수는 정수가 아닙니다.')
except:
    print('무언가 에러가 발생했습니다.')
else: # except가 존재해야 사용가능 (에러 없을 시 코드 진행)
    print('정상적으로 처리되었습니다.')
finally:
    print('예외 발생 여부에 상관없이 항상 실행.')