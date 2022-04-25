# testCase = int(input())
# lis = []
# repetition test in range(testCase):
#     A, B = map(int, input().split())
#     lis.append([A, B])
#
# repetition test in range(testCase):
#     n = lis[test][0] + lis[test][1]
#     print('Case #{0}: {1}'.format(test+1, n))

# testCase = int(input())
# lis = []
# repetition test in range(testCase):
#     A, B = map(int, input().split())
#     lis.append([A, B])
#
# repetition test in range(testCase):
#     n = lis[test][0] + lis[test][1]
#     print('Case #{0}: {1} + {2} = {3}'.format(test+1, lis[test][0], lis[test][1], n))

# import datetime
# print(str(datetime.datetime.now())[:10])



# f = 4.71
# print('%.1f' % int(round(f)))
#
# one = "hello"
# two = "python"
# print('{0}! {1}'.format(one, two))
#
# one = "python"
# two = 'java'
# three = one + '! ' + two + ' '
# print(three*3)
# print(('{0}! {1}  '.format(one, two)) * 4)
#
# lang = 'python'
# print(lang[0], lang[-1])
#
# license_plate = "24가 2210"
# print(license_plate[-4:])
# lis = license_plate.split(' ')
# print(lis[1])
#
# string = '121212'
# print(string[0::2])
#
# string = 'python'
# print(string[::-1].upper())
#
# phone_number = '010-1111-2222'
# print(phone_number.replace('-', ''))
#
# string = 'abcd'
# print(string.title())
# print(string.replace('a', 'A'))
#
# string = '국어 영어 수학 과학 경제 지리 물리 화학 생물'
# list_01 = string.split()
# print(list_01)
# repetition i in range(len(list_01)):
#     print(list_01[i])
#
# print(string.replace(' ', '\n'))




########### list
# movie_rank = ['doctor', 'split', 'lucky']
# movie_rank.append('batman')
# print(movie_rank)
#
# movie_rank.insert(1, 'superman')
# print(movie_rank)
#
# movie_rank.remove('lucky')
# print(movie_rank)
#
# del movie_rank[2:]
# print(movie_rank)
#
# lang1 = ['c', 'c++', 'java']
# lang2 = ['python', 'go', 'c#']
#
# langs = lang1 + lang2
# print(langs)
#
# nums = [num+1 repetition num in range(7)]
# print('max: {0}\nmin: {1}'.format(max(nums), min(nums)))
#
# nums = [num+1 repetition num in range(5)]
# print(sum(nums))
#
# cook = [num+1 repetition num in range(35)]
# print(len(cook))
#
# nums = [num+1 repetition num in range(5)]
# print(sum(nums) / len(nums))
#
# price = [num + 1 repetition num in range(10)]
# price.insert(0, '202044021')
# print(price[1:])
#
# price = [num + 1 repetition num in range(10)]
# print(price[1::2])
# print(price[::-1])
#
# interest = ['samsung', 'lg', 'naver']
# print(interest[0], interest[2])
#
# interest.append('sk')
# interest.append('daewoo')
# print(interest)
# print(' '.join(interest))
#
# print('/'.join(interest))
#
# print('\n'.join(interest))
#
# string = 'samsung/lg/naver'
# dict = string.split('/')
# print(dict)
#
# string = string+'/sk/daewoo'
# print(string.split('/'))


# ######## tuple
# movie_rank = ('doctor', 'split', 'lucky')
# print(f'movie_rank : {movie_rank}')
#
# t = 1, 2, 3, 4
# print(type(t))
#
# interest = ('samsung', 'lg', 'sk')
# list1 = list(interest)
# print(list1)
#
# tu = tuple(list1)
# print(tu)

########### Dictionary
# temp = {}
# dict1 = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# print(dict1)
#
# dict1['죠스바'] = 1200
# dict1['월드콘'] = 1500
# print(dict1)
#
# print('메로나 가격 : {0}'.format(dict1['메로나']))
#
# dict1['메로나'] = 1300
# print(dict1)
# del dict1['메로나']
# print(dict1)
#
# price = {'메로나':1000, '폴라포':1200}
# stock = {'메로나':10, '폴라포':3}
#
# print('메로나 {0}원 재고 {1}개'.format(price['메로나'], stock['메로나']))
# print('폴라포 {0}원 재고 {1}개'.format(price['폴라포'], stock['폴라포']))
#
# stock['폴라포'] = 2
#
# dict2 = price.copy()
# dict2.update(stock)
# print(dict2)
# import random

# inventory = {'메로나':[300, 20], '비비빅':[400,3], '죠스바':[250,100]}
# print(inventory['메로나'][0])
# print(inventory['메로나'][1])
#
# inventory['월드콘'] = [500, 7]
# print(inventory)
#
# icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
# key_list = list(icecream.keys())
# value_list = list(icecream.values())
# print(key_list)
# print(value_list)
#
# print(sum(icecream.values()))
#
# new_product = {'팥빙수':2700, '아맛나':1000}
#
# icecream.update(new_product)
# print(icecream)
#
# keys = ("apple", "pear", "peach")
# values = (300, 250, 400)
# print(dict(zip(keys, values)))



################ if/random
# import random
# x = random.randrange(0, 2)
# if x!=0 :
#     print('정답')
# else:
#     print('노답')
#
# x = random.randrange(-1, 2)
# if x > 0:
#     print('양수')
# elif x<0:
#     print('음수')
# else:
#     print('0')
#
# x = 'ab'
# if x[0] == 'a' :
#     print(len(x))
#
# x = random.randrange(1, 4)
# if x % 3 == 0:
#     print('3의 배수')
# else:
#     print(x)
# x = random.randrange(4, 16)
# if x > 3 and x <= 10:
#     print(x)
# else:
#     print('x')
#
# if x % 3 == 0 and x % 4 == 0:
#     print('정답', x)
# else :
#     print(x)

# s = input()
# print(s*2)
#
# try:
#     s = int(input())
#     print(s+10)
# except:
#     print('정수를 입력하십시오.')

# import datetime
# now = str(datetime.datetime.now())[:10]
# print(now)
#
# fruits = ['apple', 'grape', 'hongsi']
# s = input()
# if s in fruits :
#     print('정답')
# else:
#     print('오답')

# a, b = map(int, input().split())
# if a > b :
#     print(a)
# elif b > a :
#     print(b)
# else:
#     print('same')

# try:
#     addr_number = int(input())
#     print(len(str(addr_number)))
#     if len(str(addr_number)) == 5 :
#         if str(addr_number[2]) in ['0', '1', '2'] :
#             print('강북구')
#         elif addr_number[2] in [3, 4, 5] :
#             print('도봉구')
#         elif addr_number[2] in [6, 7, 8, 9] :
#             print('노원구')
#     else :
#         print('알 수 없음')
# except ValueError as e :
#     print(e)
# except IndexError as e:
#     print(e)
# except SyntaxError as e:
#     print(e)
# except Exception as e:
#     print('에러 발생' , e)




