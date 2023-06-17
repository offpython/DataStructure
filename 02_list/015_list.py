# # 리스트 아이템 순서 뒤집기
# ## reverse() 함수를 이용하면 아이템 순서를 뒤집을 수 있다. (정렬X)
#
# names = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
# print('names : {}'.format(names))
#
# names.reverse()
# print('names : {}'.format(names))
#
# ## 숫자형도 가능
# numbers = [2, 50, 0.12, 1, 9, 17, 35, 100, 3.14]
# print('numbers : {}'.format(numbers))
#
# numbers.reverse()
# print('numbers : {}'.format(numbers))

# 실습1
## 암호를 해독하는 프로그램
secret = '27156231'
secretList = []
solvedList = ''

for cha in secret:
    secretList.append(int(cha))

secretList.reverse()
print(f'secretList : {secretList}')

val = secretList[0] * secretList[1]
secretList.insert(2, val)
print(secretList)

val = secretList[3] * secretList[4]
secretList.insert(5, val)
print(secretList)

val = secretList[6] * secretList[7]
secretList.insert(8, val)
print(secretList)

val = secretList[9] * secretList[10]
secretList.insert(11, val)
print(f'secretList : {secretList}')