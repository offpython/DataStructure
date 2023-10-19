# 리스트의 곱셈 연산
students = ['홍길동', '박찬호', '이용구']
print(students)
mul = students*3
print(mul)

numbers = [2, 50, 0.12, 3, 9]
print(numbers)
mul = numbers * 2
print(mul)

# 아이템 위치 찾기
students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '김지은', '강호동']
searchIdx = students.index('강호동')
searchIdx = students.index('강호동', 2, 7)
print(searchIdx)

import random

sampleList = random.sample(range(1, 11), 10)
selectIdx = int(input('숫자 7의 위치 입력 : '))
searchIdx = sampleList.index(7)

if searchIdx == selectIdx:
    print('빙고!')
else:
    print('ㅜㅜ')

print(sampleList)
print(searchIdx)

# 특정 아이템 개수 알아내기
students = ['홍길동', '강호동', '박찬호', '이용규', '강호동', '박승철', '김지은']
searchCnt = students.count('강호동')
print(searchCnt)
searchCnt = students.count('홍길동')
print(searchCnt)
searchCnt = students.count('나나')
print(searchCnt)

# 특정 아이템 삭제
students = ['홍길동', '강호동', '박찬호', '이용규', '강호동', '박승철', '김지은']
del students[0]
print(students)

del students[2]
print(students)

del students[3:]
print(students)

import random

types = ['A', 'B', 'C', 'AB']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

for type in types:
    print(f'{type}형 -> {todayData.count(type)}명')
