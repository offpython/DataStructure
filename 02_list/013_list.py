# 리스트 연결
## extend() 함수를 이용하면 리스트에 또 다른 리스트를 연결(확장) 할 수 있다.
### a (+ b) => a 확장
names1 = ['홍길동', '박찬호', '이용규']
names2 = ['강호동', '박승철', '김지은']
print(f'names1 : {names1}')
print(f'names2 : {names2}')

names1.extend(names2)
print(f'names1 : {names1}')
print(f'names2 : {names2}') # 변함없음

## 덧셈 연산자를 이용해서 리스트를 연결할 수도 있다.
### a + b => c
names1 = ['홍길동', '박찬호', '이용규']
names2 = ['강호동', '박승철', '김지은']
names3 = names1 + names2

print(f'names3 : {names3}')
print(f'names1 : {names1}') # 변함없음
print(f'names2 : {names2}') # 변함없음

# 실습1
myFavoriteNumbers = [1, 3, 5, 6, 7]
friendFavoriteNumbers = [2, 3, 5, 8, 10]
print(f'myFavoriteNumbers: {myFavoriteNumbers}')
print(f'friendFavoriteNumbers: {friendFavoriteNumbers}')

addList = myFavoriteNumbers + friendFavoriteNumbers
print(f'addList: {addList}')

result = []
for number in addList:
    if number not in result:
        result.append(number)

print('result : {}'.format(result))