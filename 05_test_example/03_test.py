# 리스트(03)

## 1일 총 입장객이 100이라고 할 때, 전체 입장 요금을 구하는 프로그램
## 단, 입장 고객의 나이는 난수를 이용한다.

import random

visitors = []

for i in range(100):
    visitors.append(random.randint(1, 100)) # 나이
# print(visitors) # 방문객 나이 확인

group1, group2, group3, group4, group5 = 0, 0, 0, 0, 0

for age in visitors:

    if age > 0 and age <= 7:
        group1 += 1
    elif age > 8 and age <= 13:
        group2 += 1
    elif age > 14 and age <= 19:
        group3 += 1
    elif age > 20 and age <= 64:
        group4 += 1
    else:
        group5 += 1

group1Price = group1 * 0
group2Price = group2 * 200
group3Price = group3 * 300
group4Price = group4 * 500
group5Price = group5 * 0

print('-'*30)
print(f'영유아\t : {group1}명\t, 요금 : {group1Price}원')
print(f'어린이\t : {group2}명\t, 요금 : {group2Price}원')
print(f'청소년\t : {group3}명\t, 요금 : {group3Price}원')
print(f'성인\t\t : {group4}명\t, 요금 : {group4Price}원')
print(f'어르신\t : {group5}명\t, 요금 : {group5Price}원')
print('-'*30)
sum = group1Price + group2Price + group3Price + group4Price + group5Price
print(f'총 합계\t : {format(sum, ",")}원')
print('-'*30)      