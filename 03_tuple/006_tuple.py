# 튜플 슬라이싱
## [m:n]
names = ('강호동', '박찬호', '이용규', '박승철', '강호동', '김지은')
print('names : {}'.format(names))
print('names[2:4] : {}'.format(names[2:4]))
print('names[:4] : {}'.format(names[:4]))
print('names[2:] : {}'.format(names[2:]))
print('names[2:-2] : {}'.format(names[2:-2]))
print('names[2:4] : {}'.format(names[-5:-2]))

numbers = (2, 50, 0.12, 1, 9, 7, 17)
print('numbers : {}'.format(numbers))
print('numbers[2:4] : {}'.format(numbers[2:4]))
print('numbers[:4] : {}'.format(numbers[:4]))
print('numbers[2:4] : {}'.format(numbers[-5:-2]))
## 슬라이싱 단계 설정
print('numbers[2:-2:2] : {}'.format(numbers[2:-2:2]))

## XXXXXX 슬라이싱을 이용한 아이템 변경은 튜플에서 사용할 수 없음 XXXXXX
# TypeError: 'tuple' object does not support item assignment
# names[1:4] = ('park', 'lee', 'gang')
# print(names)

## 리스트 -> 튜플 아이템으로 변경 가능
names = ['강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
names[1:4] = ('park', 'lee', 'park')
print('names : {}'.format(names))
print(type(names)) ## 튜플로 아이템 변경했어도 타입은 리스트

## slice() 함수를 이용해서 아이템을 슬라이싱할 수 있다.
print('slice() 사용')
print('names : {}'.format(names))
print('names : {}'.format(names[slice(2,4)]))
print('names : {}'.format(names[slice(4)])) # ~4
print('names : {}'.format(names[slice(2,len(names))]))
print('names : {}'.format(names[slice(2,len(names) - 2)]))
print('names : {}'.format(names[slice(len(names) - 5, len(names) - 2)]))

