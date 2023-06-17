# 튜플 아이템 조회
## 인덱스
names = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
print('names[0] : {}'.format(names[0]))
print('names[1] : {}'.format(names[1]))
print('names[2] : {}'.format(names[2]))
print('names[3] : {}'.format(names[3]))
print('names[4] : {}'.format(names[4]))

numbers = (10, 20, 30, 40, 50)
print('numbers[0] : {}'.format(numbers[0]))
print('numbers[1] : {}'.format(numbers[1]))
print('numbers[2] : {}'.format(numbers[2]))
print('numbers[3] : {}'.format(numbers[3]))
print('numbers[4] : {}'.format(numbers[4]))

# 실습1
students = ('김성애', '신경도', '박기준', '최승철', '황동석')
print('--인덱스가 짝수인 녀석--')
print('students[0] : {}'.format(students[0]))
print('students[2] : {}'.format(students[2]))
print('students[4] : {}'.format(students[4]))
print('--인덱스가 홀수인 녀석')
print('students[1] : {}'.format(students[1]))
print('students[3] : {}'.format(students[3]))

for i in range(len(students)):
    if i % 2 == 0:
        print('--인덱스 짝수 students[{}] {}--'.format(i, students[i]))
    else:
        print('--인덱스 홀수 students[{}] {}--'.format(i, students[i]))