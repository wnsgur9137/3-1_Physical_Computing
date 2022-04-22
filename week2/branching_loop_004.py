ages = []
price = 0
kids = 0
mids = 0
adults = 0
humans = int(input('몇 분이 오셨죠? '))
for i in range(humans):
    ages.append(int(input('나이는? ')))

for age in ages:
    if 0 <= age < 8:
        price += 5000
        kids += 1
    elif 8 <= age < 19:
        price += 9000
        mids += 1
    elif age >= 19:
        price += 11000
        adults += 1
    else:
        print('정확한 나이를 입력해주세요')

print('=' * 50)
# print('kids = '+str(kids)+'\tmids = '+str(mids)+'\tadults = '+str(adults))
# print('총 인원 : '+str(humans))
# print('총 금액은 ' + str(price) + '원 입니다.')

print('어린이 : {0}\t청소년 : {1}\t성인 : {2}'.format(kids, mids, adults))
print('총 인원 : {0}'.format(humans))
print('총 금액 : {0}원'.format(price))

print('어린이 : %d\t 청소년 : %d\t성인 : %d' % kids, mids, adults)
print('총 인원 : %d' % humans)
print('총 금액 : %d' % price)
print('=' * 50)