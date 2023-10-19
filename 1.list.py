# 리스트
name = '홍길동'
print(f'name : {name}')

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(f'students : {students}')

numbers = [10, 20, 30, 40, 50, 60, 70]
print(f'numbers : {numbers}')

str = [2.34, '십', 20, 'one', '3.141592']
print(f'str : {str}')

# 리스트 아이템 조회
print(students[0])
print(type(students))
print(type(students[0]))

for i in range(5):
    if i % 2 == 0:
        print('인덱스가 짝수 -> students[{}] : {}'.format(i, students[i]))
    else:
        print('인덱스가 홀수 -> students[{}] : {}'.format(i, students[i]))

# 리스트 길이
sLength = len(students)
print('length of students : {}'.format(sLength))

str = 'hello python!!'
print(len(str))

for i in range(len(students)):
    print(students[i])

sports = ['수영', '배구', '농구', '조깅']
n = 0
while n < len(sports):
    print(sports[n])
    n += 1

# 리스트와 for문
cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']
for car in cars:
    print(car)

studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]
sum = 0
avg = 0
for classNo, cnt in studentCnts:
    print(f'{classNo}반 학생수 : {cnt}명')
    sum += cnt
    avg = sum/len(studentCnts)
print(f'전체 학생 수 : {sum}명')
print(f'평균 학생 수 : {avg}명')

minScore = 60
scores = [
    ['국어', 58],
    ['영어', 77],
    ['수학', 89],
    ['과학', 99],
    ['국사', 50]]

for score in scores:
    if score[1] < minScore:
        print(f'과락 과목 : {score[0]} -> 점수 : {score[1]}')

for subject, score in scores:
    if score < minScore:
        print(f'과락 과목 : {subject} -> 점수 : {score}')

for subject, score in scores:
    if score >= minScore: continue
    print(f'과락 과목 : {subject} -> 점수 : {score}')

# 리스트와 while문
cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

n = 0
while n < len(cars):
    print(cars[n])
    n += 1
n= 0
flag = True
while flag:
    print(cars[n])
    n += 1
    if n == len(cars):
        flag = False
n = 0
while True:
    print(cars[n])
    n += 1
    if n == len(cars):
        break

studentCnts = [1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]
sum = 0
avg = 0
n = 0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print(f'{classNo}반 학생 수 : {cnt}')
    sum += cnt
    n += 1

print(f'전체 학생 수 : {sum}명')
print(f'평균 학생 수 : {sum/len(studentCnts)}명')

minScore = 60
scores = [
    ['국어', 58],
    ['영어', 77],
    ['수학', 89],
    ['과학', 99],
    ['국사', 50]]

n = 0
while n < len(scores):
    if scores[n][1] < minScore:
        print(f'과락 과목 : {scores[n][0]}, {scores[n][1]}점')
    n += 1

n = 0
while n < len(scores):
    if scores[n][1] >= minScore:
        n += 1
        continue
    print(f'과락 과목 : {scores[n][0]}, {scores[n][1]}점')
    n += 1

studentCnts = [1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]

minClassNo = 0; maxClassNo = 0;
minCnt = 0; maxCnt = 0;

n = 0
while n < len(studentCnts):
    if minCnt == 0 or minCnt > studentCnts[n][1]:
        minClassNo = studentCnts[n][0]
        minCnt = studentCnts[n][1]
    if maxCnt < studentCnts[n][1]:
        maxClassNo = studentCnts[n][0]
        maxCnt = studentCnts[n][1]
    n += 1
print(f'학생 수가 가장 적은 반 : {minClassNo}반, {minCnt}명')
print(f'학생 수가 가장 적은 반 : {maxClassNo}반, {maxCnt}명')


