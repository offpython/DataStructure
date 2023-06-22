# 리스트(04)

## 친구 이름 다섯 명을 리스트에 저장하고 오름차순과 내림차순으로 정렬

# friendsName = []
#
# for i in range(5):
#     friendsName.append(input('친구 이름 입력 : '))
#
# print(f'친구들 : {friendsName}')
# friendsName.sort()
# print(f'오름차순 : {friendsName}')
# friendsName.sort(reverse=True)
# print(f'내림차순 : {friendsName}')

## 다음 리스트에서 중복 아이템(숫자)를 제거하는 프로그램 만드릭
numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numbers : {numbers}')

idx = 0
while True:
    if idx >= len(numbers):
        break

    if numbers.count(numbers[idx]) >= 2:
        numbers.remove(numbers[idx])
        continue

    idx += 1

print(f'numbers : {numbers}')
