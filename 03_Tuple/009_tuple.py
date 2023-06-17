# 튜플과 for문(1)

## for문을 이용하면 튜플의 아이템을 자동으로 참조할 수 있다.
cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

for i in range(len(cars)):
    print(cars[i])

for car in cars:
    print(car)

## for문을 이용한 내부 튜플 조회
studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

for i in range(len(studentCnts)):
    print('{}학급 학생 수 : {}'.format(studentCnts[i][0], studentCnts[i][1]))

for classNo, cnt in studentCnts:
    print('{}반 학생 수 : {}'.format(classNo, cnt))

# 실습1
## 학급별 학생 수와 전체 학생 수, 평균 학생 수 출력
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
print('studentCnts  : {}'.format(studentCnts))

sum = 0
avg = 0

for classNo, cnt in studentCnts:
    print('{}학급 학생수 : {}명'.format(classNo, cnt))
    sum += cnt

print('전체 학생 수 : {}'.format(sum))
print('전체 학생 수 : {}'.format(sum/len(studentCnts)))
