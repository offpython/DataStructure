# 리스트와 for문_1

# for문을 이용하면 리스트의 아이템을 자동으로 참조할 수 있다.
cars = ['그랜저', '소나타', '말리부', '카니발', '소렌토']

# 방법1_인덱스 이용
for i in range(len(cars)):
    print(cars[i])

# 방법2_car변수 이용
for i in cars:
    print(i)

# for문을 이용하면 리스트 내부에 또 다른 리스트의 아이템을 조회할 수도 있다.
studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

for i in range(len(studentCnts)):
    print('{}학급 학생 수 : {}'.format(studentCnts[i][0], studentCnts[i][1]))

for classNo, cnt in studentCnts:
    print('{}반 학생 수 : {}'.format(classNo, cnt))

# 실습1
studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
sum = 0
avg = 0

for classNo, cnt in studentCnts:
    print('1학년 {}반 학생 수 : {}'.format(classNo, cnt))
    sum += cnt

print(f'전체 학생 수 : {sum}')
print(f'평균 학생 수 : {sum/len(studentCnts)}')

    
