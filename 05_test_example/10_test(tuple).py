# 튜플(05)

## 학금별 학생 수를 나타낸 튜플을 이용해서 , 요구사항에 맞는 데이터 출력
## 전체학생수/평균학생수/학생 수가 가장 적은 학급/학생 수가 가장 많은 학급/학급별 학생 편차

studentCnt = (
    {'cls01':18},
    {'cls02':21},
    {'cls03':20},
    {'cls04':19},
    {'cls05':22},
    {'cls06':20},
    {'cls07':23},
    {'cls08':17},
)

totalCnt = 0
minStuCnt = 0; minCls = ''
maxStuCnt = 0; maxCls = ''
deviation = [] #편차

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        totalCnt = totalCnt + v

        if minStuCnt == 0 or minStuCnt > v:
            minStuCnt = v
            minCls = k

        if maxStuCnt < v:
            maxStuCnt = v
            maxCls = k

print(f'전체 학생 수 : {totalCnt}')
avgCnt = totalCnt / len(studentCnt)
print(f'평균 학생 수 : {avgCnt}')
print(f'학생 수가 가장 적은 학급 : {minCls}({minStuCnt}명)')
print(f'학생 수가 가장 많은 학급 : {minCls}({minStuCnt}명)')

#편차
for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        deviation.append(v - avgCnt)

print(f'학급별 학생 편차 : {deviation})')

