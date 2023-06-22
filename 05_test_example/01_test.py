# 리스트(01)

## 1부터 사용자가 입력한 숫자까지 약수와 소수를 리스트에 각각 저장하고, 출력하는 프로그램

inputNum = int(input('1보다 큰 정수 입력 : '))
listA = [] # 약수
listB = [] # 소수

# 약수
for n in range(1, inputNum + 1):
    if n == 1:
        listA.append(n)
    else:
        if inputNum % n == 0:
            listA.append(n)

print(f'{inputNum}의 약수 : {listA}')

# 소수
for number in range(2, inputNum + 1):

    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break
    if flag:
        listB.append(number)

print(f'{inputNum}의 소수 : {listB}')