
# 컴퓨터정보과 3학년 A반 202044021 이준혁
# 피지컬컴퓨팅 중간고사

# 좌석 미해결

movie_1917_dict = {'08:00':[0, 90],
                   '13:00':[0, 90],
                   '18:00':[0, 90]}

movie_mugando_dict = {'08:00':[0, 140],
                   '13:00':[0, 140],
                   '18:00':[0, 140]}

movie_tajja_dict = {'11:00':[0, 90],
                   '15:00':[0, 90],
                   '21:00':[0, 90]}

movie_spon_dict = {'11:00':[0, 140],
                   '15:00':[0, 140],
                   '21:00':[0, 140]}

# 총 영화의 수
list_movie_count = 4

# 예매 인원 및 연령
person_age_count_list = []

# 메인 선택 메뉴
def menu() :
    print('=' * 20)
    print('1. 영화 예매')
    print('2. 프로그램 종료')
    print('=' * 20)


# 영화 메뉴 출력
def movie_menu():
    print('=' * 20)
    print('1. 1917 \t/\t 15세 관람가 \t/\t A관')
    print('2. 무인도 \t/\t 12세 관람가 \t/\t B관')
    print('3. 타짜 \t\t/\t 18세 관람가 \t/\t A관')
    print('4. 스폰지밥 극장판 \t/\t 전체 이용가 \t/\t B관')
    print('=' * 20)


# 영화 선택
def movie_choice():
    choice_movie = int(input('관람하실 영화를 선택해 주세요: '))
    if choice_movie == 1:
        time_choice('1917')
    elif choice_movie == 2:
        time_choice('mugando')
    elif choice_movie == 3:
        time_choice('tajja')
    elif choice_movie == 4:
        time_choice('spon')
    else:
        print('메뉴에서 선택해 주십시오.')
        movie_choice()


# 시간대 선택
def time_choice(movie):

    movie_dict = {}

    if movie == '1917':    # A관
        print('1.\t 08:00 \t {0} / {1}'.format(movie_1917_dict['08:00'][0],movie_1917_dict['08:00'][1]))
        print('2.\t 13:00 \t {0} / {1}'.format(movie_1917_dict['13:00'][0], movie_1917_dict['13:00'][1]))
        print('3.\t 18:00 \t {0} / {1}'.format(movie_1917_dict['18:00'][0], movie_1917_dict['18:00'][1]))
        movie_dict = movie_1917_dict
    elif movie == 'mugando':    # B관
        print('1.\t 08:00 \t {0} / {1}'.format(movie_mugando_dict['08:00'][0], movie_mugando_dict['08:00'][1]))
        print('2.\t 13:00 \t {0} / {1}'.format(movie_mugando_dict['13:00'][0], movie_mugando_dict['13:00'][1]))
        print('3.\t 18:00 \t {0} / {1}'.format(movie_mugando_dict['18:00'][0], movie_mugando_dict['18:00'][1]))
        movie_dict = movie_mugando_dict
    elif movie == 'tajja':    # A관
        print('1.\t 11:00 \t {0} / {1}'.format(movie_tajja_dict['11:00'][0],movie_tajja_dict['11:00'][1]))
        print('2.\t 15:00 \t {0} / {1}'.format(movie_tajja_dict['15:00'][0],movie_tajja_dict['15:00'][1]))
        print('3.\t 21:00 \t {0} / {1}'.format(movie_tajja_dict['21:00'][0], movie_tajja_dict['21:00'][1]))
        movie_dict = movie_tajja_dict
    elif movie == 'spon':    # B관
        print('1.\t 11:00 \t {0} / {1}'.format(movie_spon_dict['11:00'][0],movie_spon_dict['11:00'][1]))
        print('2.\t 15:00 \t {0} / {1}'.format(movie_spon_dict['15:00'][0],movie_spon_dict['15:00'][1]))
        print('3.\t 21:00 \t {0} / {1}'.format(movie_spon_dict['21:00'][0],movie_spon_dict['21:00'][1]))
        movie_dict = movie_spon_dict
    else:
        print('에러')


    movie_time = int(input('관람하실 시간을 선택해주십시오: '))
    if movie_time > len(movie_dict.keys()) or movie_time < 0:
        print('보기에서 선택해 주십시오.')
        time_choice(movie)

    person_count(movie, movie_time)


# 인원 입력
def person_count(movie, movie_time):

    person = 0

    if movie == '1917': # 15세 관람가
        person = int(input('몇 분이서 오셨습니까?: '))
        for idx in range(person):
            age = int(input('나이는?: '))
            check = age_check('1917', age)
            if check == False:
                print('15세 관람가 입니다.')
                main()
            person_age_count_list.append(age)

    elif movie == 'mugando':
        person = int(input('몇 분이서 오셨습니까?: '))
        for idx in range(person):
            age = int(input('나이는?: '))
            check = age_check('mugando', age)
            if check == False:
                print('12세 관람가 입니다.')
                main()
            person_age_count_list.append(age)

    elif movie == 'tajja':
        person = int(input('몇 분이서 오셨습니까?: '))
        list = []
        for idx in range(person):
            age = int(input('나이는?: '))
            check = age_check('tajja', age)
            if check == False:
                print('18세 관람가 입니다.')
                main()
            person_age_count_list.append(age)

    elif movie == 'spon':
        person = int(input('몇 분이서 오셨습니까?: '))
        list = []
        for idx in range(person):
            age = int(input('나이는?: '))
            check = age_check('spon', age)
            person_age_count_list.append(age)
    else:
        print('에러')

    cheet_choice(movie, movie_time, person)


# 연령 체크
def age_check(movie, age):
    if movie == '1917': # 15세 관람가
        if age < 15:
            return False
        else:
            return True
    elif movie == 'mugando': # 12세 관람가
        if age < 12:
            return False
        else:
            return True
    elif movie == 'tajja': # 18세 관람가
        if age < 18:
            return False
        else:
            return True
    elif movie == 'spon': # 전체이용가
        pass


# 좌석 선택
def cheet_choice(movie, movie_time, person):
    if movie == '1917':
        pass
    elif movie == 'mugando':
        pass
    elif movie == 'tajja':
        pass
    elif movie == 'spon':
        pass

    print_price(movie, movie_time)


# 계산 및 영수증
def print_price(movie, movie_time):

    movie_place = ''

    if movie == '1917' or movie == 'tajja':
        movie_place = 'A관'
    else :
        movie_place = 'B관'

    child = 0
    teenage = 0
    adult = 0

    print(type(person_age_count_list))
    print(person_age_count_list)
    print(len(person_age_count_list))

    for age in person_age_count_list:
        if age < 12:
            child = child + 1
        elif age < 17:
            teenage = teenage + 1
        else:
            adult = adult + 1

    print('='*20)
    print('총 인원: {0}, (어린이: {1}명, 청소년 {2}명, 성인 {3}명)'
          .format(len(person_age_count_list), child, teenage, adult))

    price = (child * 5000) + (teenage * 9000) + (adult * 11000)
    print('\n총 금액: {0}'.format(price))

    print_paper = input('영수증을 출력하시겠습니까? (Y/N): ')
    if print_paper.upper() == 'Y':
        try:
            fp = open('receipt.txt', 'w')
            print('영화: {0}'.format(movie), file=fp)
            print('상영관: {0}'.format(movie_place), file=fp)
            print('\n<영수증>', file=fp)
            print('총 인원: {0}, (어린이: {1}명, 청소년 {2}명, 성인 {3}명)'
                  .format(len(person_age_count_list), child, teenage, adult), file=fp)
            print('\n총 금액: {0}'.format(price), file=fp)
        except:
            print('영수증 출력 에러')
        finally:
            fp.close()
    else:
        pass


# 메인함수
def main():
    acti = True

    menu()

    choice_menu = int(input('원하시는 메뉴를 선택해 주십시오 : '))

    if choice_menu == 1:
        movie_menu()
        movie_choice()
    elif choice_menu == 2:
        print('키오스크 종료')
        exit()
    else:
        print('메뉴에서 선택해 주십시오.')


# 메인함수 호출(프로그램 시작 시)
if __name__ == '__main__':
    main()


