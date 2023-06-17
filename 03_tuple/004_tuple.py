# 튜플 길이
## 튜플에 저장된 아이템 갯수를 튜플 길이라고 한다.
students= ('홍길동','박찬호', '이용규', '박승철', '김지은')
sLength = len(students)
print('studentsTuple : {}'.format(students))
print('sLength : {}'.format(sLength))

## len()을 이용한 조회
### len()과 반복문을 이용하면 튜플의 아이템 조회가 가능하다.

# for문
for i in range(len(students)):
    print('index number : {}'.format(i))
    print('students[{}] : {}'.format(i, students[i]))

# while문
n = 0
sLength = len(students)

while n < len(students):
    print('index number_{}'.format(n))
    print('students[{}]_{}'.format(n, students[n]))
    n += 1

for student in students:
    print('student : {}'.format(student))

# 실습1
myFavoriteSports = ('수영', '배구', '야구', '조깅')

for i in range(len(myFavoriteSports)):
    print('myFavoriteSports[{}]: {}'.format(i, myFavoriteSports[i]))

n = 0
sLength = len(myFavoriteSports)

while n < sLength:
    print('myFavoriteSports[{}] -> {}'.format(n, myFavoriteSports[n]))
    n += 1

for i in myFavoriteSports:
    print('myFavoriteSports : {}'.format(i))

