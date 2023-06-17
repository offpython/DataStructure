# 딕셔너리 수정
## '딕셔너리이름[키] = 값' 형태로 아이템 수정

myInfo = {}

myInfo['이름'] = '박경진'
myInfo['전공'] = 'computer'
myInfo['메일'] = 'jin@naver.com'
myInfo['학년'] = 3
myInfo['주소'] = '대한민국 서울'
myInfo['취미'] = ['요리', '여행']
print(myInfo)

myInfo['메일'] = 'jin@gmail.com'
print(myInfo)

# 실습1
## 학생의 시험 점수가 60점 미만이면 'F(재시험)'으로 값을 변경
scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores : {scores}')

minScore = 60
fStr = 'F(재시험)'
if scores['kor'] < minScore:
    scores['kor'] = fStr
if scores['eng'] < minScore:
    scores['eng'] = fStr
if scores['mat'] < minScore:
    scores['mat'] = fStr
if scores['sci'] < minScore:
    scores['sci'] = fStr
if scores['his'] < minScore:
    scores['his'] = fStr
print(f'scores : {scores}')

# 실습2
## 하루에 몸무게와 신장이 각각 -0.3kg +0.001m씩 변한다고 할 때,
## 30일 이후의 몸무게와 신장 값을 저장하고 BMI 값도 출력하는 프로그램
## (현재 신체정보는 아래 딕셔너리에 저장되어 있다.)
myBodyInfo = {'이름':'gildong', '몸무게':83.0, '신장':1.8}
myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
print(f'myBodyInfo : {myBodyInfo}')
print(f'myBMI : {round(myBMI, 2)}')

date = 0
while True:
    date += 1

    myBodyInfo['몸무게'] = round((myBodyInfo['몸무게'] - 0.3), 2)
    print('몸무게 : {}kg'.format(myBodyInfo['몸무게']))

    myBodyInfo['신장'] = round((myBodyInfo['신장'] + 0.001), 3)
    print('신장 : {}cm'.format(myBodyInfo['신장']))

    myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)

    if date >= 30:
        break

print(f'myBodyInfo : {myBodyInfo}')
print(f'myBMI : {round(myBMI, 2)}')



