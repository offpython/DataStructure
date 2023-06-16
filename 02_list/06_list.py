# 리스트와 while문_1

# while문 이용하면 다양한 방법으로 아이템 조회가 가능하다.
cars = ['그랜저', '소나타','말리부','카니발','쏘렌토']

# 방법 1
n = 0
while n < len(cars):
    print(cars[n])
    n += 1

# 방법 2
n = 0
flag = True
while flag:
    print(cars[n])
    n += 1

    if n == len(cars):
        flag = False

# 방법 3
n = 0
while True:
    print(cars[n])
    n += 1

    if n == len(cars):
        break

# 실습1
studentsCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

sum = 0
avg = 0
n = 0
while n < len(studentsCnts):
    classNo = studentsCnts[n][0]
    cnt = studentsCnts[n][1]
    print('{}학급 학생 수 : {}'.format(classNo, cnt))

    sum += cnt
    n += 1

print('전체 학생 수 : {}명'.format(sum))
print('평균 학생 수 : {}명'.format(sum/len(studentsCnts)))



