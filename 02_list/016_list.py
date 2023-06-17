# 리스트 슬라이싱
## [n:m]을 이용하면 리스트에서 원하는 아이템만 뽑아낼 수 있다.

names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('names : {}'.format(names))
print('names : {}'.format(names[2:4]))
print('names : {}'.format(names[:4]))
print('names : {}'.format(names[2:]))
print('names : {}'.format(names[2:-2]))
print('names : {}'.format(names[-5:-2 ]))

numbers = [2, 50, 0.12, 1, 9, 7, 17, 100, 3.14]
print('numbers : {}'.format(numbers))
print('numbers : {}'.format(numbers[2:4]))
print('numbers : {}'.format(numbers[:4]))
print('numbers : {}'.format(numbers[2:]))
print('numbers : {}'.format(numbers[2:-2]))
print('numbers : {}'.format(numbers[-5:-2]))
## 슬라이싱할 떄 단계를 설정할 수 있다.
print('numbers : {}'.format(numbers[2:-2: 2])) # 2 <= -2에서 2step씩 뽑음
print('numbers : {}'.format(numbers[:-2:2])) # 처음 ~ -2에서 2step씩 뽑음
print('numbers : {}'.format(numbers[::2])) # 전체에서 2step씩 뽑음

str = 'abcdefghijklmnopqrstuvwxyz'
print('str : {}'.format(str))
print('str : {}'.format(str[2:4]))
print('str : {}'.format(str[:4]))
print('str : {}'.format(str[2:]))
print('str : {}'.format(str[2:-2]))
print('str : {}'.format(str[-5:-2 ]))

## 슬라이싱을 통한 아이템 변경
names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('names : {}'.format(names))

names[1:4] = ['park', 'lee', 'gang']
print('names : {}'.format(names))

## slice() 함수를 이용해서 아이템을 슬라이싱할 수 있다.
print('slice() 사용')
print('names : {}'.format(names))
print('names : {}'.format(names[slice(2,4)]))
print('names : {}'.format(names[slice(4)])) # ~4
print('names : {}'.format(names[slice(2,len(names))]))
print('names : {}'.format(names[slice(2,len(names) - 2)]))
print('names : {}'.format(names[slice(len(names) - 5, len(names) - 2)]))

