# 튜플 결합
name1 = ('홍길동', '박찬호', '이용규')
name2 = ('박승철', '김지은', '강호동')

name3 = name1 + name2
print('name3 : {}'.format(name3))

## XXXXXX extend() 함수는 튜플에서 사용할 수 없음 XXXXXX
# AttributeError: 'tuple' object has no attribute 'extend'
# name3 = name1.extend(name2)

# 실습1
## 튜플을 이용해서 나와 친구가 좋아하는 번호를 합치되, 번호 중복없는 프로그램
myNumbers = (1, 3, 5, 6, 7)
friendNumbers = (2, 3, 5, 8, 10)
print('myNumbers : {}'.format(myNumbers))
print('friendNumbers  : {}'.format(friendNumbers))

result = myNumbers + friendNumbers
print('result : {}'.format(result))

for number in friendNumbers:
    if number not in myNumbers:
        myNumbers = myNumbers + (number, )

print('myNumbers : {}'.format(myNumbers))



