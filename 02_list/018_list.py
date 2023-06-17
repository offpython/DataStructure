# 리스트의 나머지 기능들(2)

## 특정 아이템의 개수 알아내기
### count() 함수를 이용하면 특정 아이템의 개수를 알아낼 수 있다.
names = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('names : {}'.format(names))

searchCnt = names.count('홍길동')
print('searchCnt : {}'.format(searchCnt))

searchCnt = names.count('강호동')
print('searchCnt : {}'.format(searchCnt))

searchCnt = names.count('김아무개')
print('searchCnt : {}'.format(searchCnt))

## 특정 아이템 삭제
### del 키워드를 사용하면 특정 아이템을 삭제할 수 있다.
names = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('names : {}'.format(names))

del names[1]
print('names : {}'.format(names))

del names[1:4]
print('names : {}'.format(names))

del names[2:]
print('names : {}'.format(names))

del names[:1]
print('names : {}'.format(names))

# 실습1
## 하루 동안 헌혈을 진행한 후 혈액형 별 개수를 파악하는 프로그램

import random

types = ['A', 'B', 'O', 'AB']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for type in types:
    print('{}형 : {}개'.format(type, todayData.count(type)))

