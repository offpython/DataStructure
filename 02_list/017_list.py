# 리스트의 나머지 기능들(1)

## 리스트 곱셈 연산
### 리스트를 곱셈 연산하면 아이템이 반복된다.
names = ['홍길동', '박찬호', '이용규']
print('names : {}'.format(names))

namesMul = names * 2
print('namesMul : {}'.format(namesMul))

numbers = [2, 50, 0.12, 1, 9]
numbersMul = numbers * 3
print('numbersMul : {}'.format(numbersMul)) # 리스트(아이템X) 곱셈임

## 아이템 위치 찾기
### index(item) 함수로 item의 인덱스를 알아낼 수 있다.
names = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('names : {}'.format(names))

searchIdx = names.index('강호동') # 가장 앞 것만 찾음
print('searchIdx : {}'.format(searchIdx))

searchIdx = names.index('강호동', 2, 6) # 범위(인덱스 2~6)에서 아이템찾기
print('searchIdx : {}'.format(searchIdx))

numbers = [2, 50, 0.12, 1, 9]
searchIdx2 = numbers.index(0.12)
print('searchIdx2 : {}'.format(searchIdx2))

# 실습1
## 1 ~ 10까지의 정수가 중복되지 않고 섞여있을 때, 행운의 숫자 7을 찾아라
import random

sampleList = random.sample(range(1, 11), 10)

selectIdx = int(input('숫자 7의 위치 입력 : '))
searchIdx = sampleList.index(7)

if selectIdx == searchIdx:
    print('빙고!')
else:
    print('ㅠㅠ')

print('sampleList : {}'.format(sampleList))
print('searchIdx : {}'.format(searchIdx))
