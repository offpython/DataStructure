# 튜플과 while문(1)

## while문을 이용하면 다양한 방법으로 아이템 조회가 가능하다.
cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

n = 0
while n < len(cars):
    print(cars[n])
    n += 1

n = 0
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

names = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

n = 0
while n < len(names):
    print('{}학급 학생 수 : {}'.format(names[n][0], names[n][1]))
    n += 1

# 실습1
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
print('studentCnts : {}'.format(studentCnts))

sum = 0
avg = 0

n = 0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print('{}반 학생수 : {}명'.format(classNo, cnt))

    sum += cnt
    n += 1

print('전체 학생 수 : {}'.format(sum))
print('전체 학생 수 : {}'.format(sum/len(studentCnts)))





