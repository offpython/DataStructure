# 튜플(02)

## 다음 2개 튜플에 대해서 합집합(중복X)과 교집합 출력
tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

tempHap = list(tuple1)  # 합 -> 리스트로 변경
tempGyo = list()

for n in tuple2:
    if n not in tempHap:
        tempHap.append(n)
    else:
        tempGyo.append(n)

tempHap = tuple(sorted(tempHap)) # 오름차순
tempGyo = tuple(sorted(tempGyo))

print(f'합집합(중복X)\t: {tempHap}')
print(f'교집합\t: {tempGyo}')


# while문 사용
tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)
# 튜플 합친 뒤(튜플) 리스트 변환 후 중복 제거
tempHap = tuple1 + tuple2
tempGyo = list()
tempHap = list(tempHap)

print(f'tempHap : {tempHap}')
print(f'tempGyo : {tempGyo}')

idx = 0
while True:
    if idx >= len(tempHap):
        break

    if tempHap.count(tempHap[idx]) >= 2:
        tempGyo.append(tempHap[idx])
        tempHap.remove(tempHap[idx])
        continue

    idx += 1

# 다시 튜플 변환
print(f'tempHap : {tuple(sorted(tempHap))}')
print(f'tempGyo : {tuple(sorted(tempGyo))}')