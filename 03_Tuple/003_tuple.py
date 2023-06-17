# in, not in 키워드
## in, not in 키워드를 이용하면 아이템의 존재 유/무를 알 수 있다.
studentsTuple = ('박찬호', '이용규', '박승철', '강호동', '김지은')
print('studentsTuple : {}'.format(studentsTuple))

searchName = input('학생 이름 입력 : ')

# in
if searchName in studentsTuple:
    print('{} 학생은 우리반 학생입니다.'.format(searchName))
else:
    print('{} 학생은 우리반 학생아닙니다.'.format(searchName))

# not in
if searchName not in studentsTuple:
    print('{} 학생은 우리반 학생아닙니다.'.format(searchName))
else:
    print('{} 학생은 우리반 학생입니다.'.format(searchName))

# 실습1
## 컴퓨터가 1~10까지 5개의 난수를 생성한 후,
## 사용자가 입력한 숫자가 있는지 없는지를 출력하는 프로그램
import random

randomNumbers = random.sample(range(1, 11), 5)

userNumber = int(input('숫자 입력(확률 50%) : '))
if userNumber in randomNumbers:
    print('빙고!')
else:
    print('다음 기회에~')

print('randomNumbers : {}'.format(randomNumbers))
print('userNumber : {}'.format(userNumber))

# 실습2
## 문장에 비속어가 있는지 알아내는 프로그램
wrongWord = ['쩔었다', '짭새', '먹튀','지린','쪼개다', '뒷담 까다']
sentence = '짭새 등장에 강도들은 모두 쩔었다. 그리고 강도들은 지린 듯 도망갔다.'

for word in wrongWord:
    if word in sentence:
        print('비속어 : {}'.format(word))
