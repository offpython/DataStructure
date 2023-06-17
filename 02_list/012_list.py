# 리스트의 특정 아이템 삭제
## remove() 함수를 이용하면 특정 아이템을 삭제할 수 있다.
names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print(names)

names.remove('박찬호')
print(names)

## remove()는 한 개의 아이템만 삭제 가능하다.
## 만약 삭제하려는 데이터가 2개 이상이라면 while문을 이용하자.
names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']

print('강호동' in names)

while '강호동' in names:
    names.remove('강호동')

print(names)

# 실습1
myList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']
print('일정 : {}'.format(myList))

removeLIst = input('삭제 대상 입력 : ')
myList.remove(removeLIst)
print('일정 : {}'.format(myList))

# 실습2
subjects = ['국어', '영어', '수학', '과학', '국사', '영어', '영어']
print('시험 과목표 : {}'.format(subjects))

removeSubject = input('삭제 과목명 입력 : ')
while removeSubject in subjects:
    subjects.remove(removeSubject)

print('시험 과목표 : {}'.format(subjects))
