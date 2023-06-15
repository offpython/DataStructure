# 리스트의 길이
## 리스트에 저장된 아이템 개수를 뜻한다.

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(students)
sLength = len(students)
print('length of students : {}'.format(sLength))
print(type(sLength))

# len()를 이용한 조회
# len()과 반복문을 이용하면 리스트의 아이템 조회가 가능하다.

for문
for i in range(len(students)):
    print(students[i])

# while문
n = 0
sLenghth = len(students)
while n < sLenghth:
    print('n : {}'.format(n))
    print('students[{}] : {}'.format(n, students[n]))

    n += 1

#len()함수를 이용한 조회
# len()함수는 리스트의 개수뿐만 아니라 문자열의 길이도 알 수 있다.

str = 'Hello World'
print(len(str))

# 실습1
myFavSports = ['수영', '야구', '야구', '조깅']

for item in myFavSports:
    print(item)

n = 0
while n < len(myFavSports):
    print(myFavSports[n])
    n += 1


