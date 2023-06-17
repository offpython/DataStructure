# 특정 위치에 아이템 추가하기
# insert() 함수를 이용하면 특정 위치(인덱스)에 아이템을 추가할 수 있다.

names = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
names.insert(3, '강호동')
print('names : {}'.format(names))
print('length of names : {}'.format(len(names)))
print('last index : {}'.format(len(names) - 1))

words = ['I', 'a', 'boy']
for word in words:
    print(word, end='')
print()

words.insert(1, 'am')
for word in words:
    print('{} '.format(word), end ='')

# 실습1
## 오름차순으로 정렬되어 있는 숫자들에 사용자가 입력한 정수를 추가하는 프로그램
## (단, 추가 후에도 오름차순 정렬이 유지되어야 한다.)

numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputNumber = int(input('숫자 입력 : '))
insertIdx = 0

for idx, number in enumerate(numbers):
    print(idx, number)

    if insertIdx == 0 and inputNumber < number:
        insertIdx = idx

numbers.insert(insertIdx, inputNumber)
print('numbers : {}'.format(numbers))



