# 리스트 아이템 조회

# 인덱스란, 아이템에 자동으로 부여되는 번호

# 리스트 아이템은 인덱스를 이용해서 조회 가능하다.
students = ['박찬호', 10, 3.14, ['박승철', '김지은']]
print(type(students))

print(students[0])
print(type(students[0]))
print(students[1])
print(type(students[1]))
print(students[2])
print(type(students[2]))
print(students[3])
print(type(students[3]))

# 오류_IndexError: list index out of range
print(students[5])

# 실습1
students = ['김성예', '선경도', '박기준', '최승철', '황동석']

for i in range(5):
    if i % 2 == 0:
        print('인덱스가 짝수인 경우 --> students[{}] : {}'.format(i, students[i]))
    else:
        print('인덱스가 홀수인 경우 --> students[{}] : {}'.format(i, students[i]))

