# 딕셔너리(02)

## 삼각형부터 십각형까지 내각의 합과 내각을 딕셔리에 저장하는 프로그램 만들기
## n각형의 내각의 합 공식 = 180 * (n -2)

dic = {}

for n in range(3, 11):
    hap = 180 * (n - 2)
    ang = int(hap / n)
    dic[n] = [hap, ang]

print(dic)

## 1 ~ 10까지 각각의 정수에 대한 약수를 저장하는 딕셔너리 만들기
dic = {}

for n1 in range(2, 11):
    tempList = []
    for n2 in range(1, n1 + 1):
        if n1 % n2 == 0:
            tempList.append(n2)
    dic[n1] = tempList

print(dic)
