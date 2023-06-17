# 리스트에 아이템 추가
# append() 함수를 이용하면 마지막 인덱스에 아이템을 추가할 수 있다.

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
students.append('강호동')

print(f'students : {students}')
print(f'length of students : {len(students)}')
print(f'last index : {len(students) - 1}')

scores = [['국어', 88], ['영어', 91]]
scores.append(['수학', 96])

print('scores : {}'.format(scores))
print('length of scores : {}'.format(len(scores)))
print('last index : {}'.format(len(scores) - 1))

# 실습1
myFamilyAge = [['아빠', 40], ['엄마', 38], ['나', 9]]
myFamilyAge.append(['동생', 1])

print(myFamilyAge)

for name, age in myFamilyAge:
    print('{} : {}'.format(name, age))
