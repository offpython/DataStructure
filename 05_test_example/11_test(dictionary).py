# # 딕셔너리(01)
#
# ## 과목별 점수를 딕셔너리에 저장하고 출력하는 프로그램
#
# subject = ['국어', '영어', '수학', '과학', '국사']
# scores = {}
#
# for s in subject:
#     score = int(input(s + ' 점수 입력 :'))
#     scores[s] = score
#
# print(f'과목별 점수 : {scores}')

## 사용자의 아이디, 비밀번호를 이용해서 로그인 프로그램을 만들기

members = {'urkpo': '0928^7$',
            'xxayv': '%2*9$91',
            'Usqux': '!0%) &84',
            'heums': '%@3^0%3',
            'uwemc': '85236(&',
            'iemwv': ')8!36^&',
            'sqblx': ')^2)9!',
            'jbbpy': '67269*3',
            'hikwu': '$&@@#64',
            'fvwwy': '82$%) 31'
}

memId = input('아이디 입력 : ')
memPw = input('패스워드 입력 : ')

if memId in members:
    if members[memId] == memPw:
        print('로그인 성공!!!')
    else:
        print('비밀번호 확인!!')

else:
    print('아이디 확인!!')