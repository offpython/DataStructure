# 리스트(04)

## 4개의 숫자 중 서로 다른 숫자 2개를 선택해서 만들 수 있는 모든 경우의 수를 출력하는 프로그램

numbers = [4, 6, 7, 9]
result = []

for n1 in numbers:
    for n2 in numbers:
        if n1 == n2:
            continue

        result.append([n1, n2])

print(f'result : {result}')
print(f'result 갯수 : {len(result)}')

## 순열 공식 : n1 / (n-r)!
import math
pernutation = math.factorial(len(numbers)) / math.factorial((len(numbers)) - 2)
print(f'pernutation : {int(pernutation)}') ## 경우의 수 (갯수) 만 구할 떄

# 4개의 숫자 중 서로 다른 숫자 3개를 선택해서 만들 수 있는 모든 경우의 수
numbers = [4, 6, 7, 9]
result = []

for n1 in numbers:
    for n2 in numbers:
        if n1 == n2: continue
        for n3 in numbers:
            if n1 == n3 or n2 == n3: continue

            result.append([n1, n2, n3])

        result.append([n1, n2])

print(f'result : {result}')
print(f'result 갯수 : {len(result)}')