# 튜플(tuple)
## 리스트와 비슷하지만 아이템 변경이 불가하다.

names = ('강호동', '박찬호', '이용규', '박승철', '강호동', '김지은')
print('names : {}'.format(names))
print('type : {}'.format(type(names)))
numbers = (10, 20, 30, 40, 50, 60, 70)
print('numbers : {}'.format(numbers))
print('type : {}'.format(type(numbers)))
strs = (3.14, '십', 20, 'one', '3.141592')
print('strs : {}'.format(strs))
print('type : {}'.format(type(strs)))
datas = (10, 20, 30, (40, 50, 60))
print('datas : {}'.format(datas))
print('type : {}'.format(type(datas)))

# 실습1
myFamilyNames = ('홍아빠', '홍엄마', '홍길동', '홍동생')
print('myFamilyNames : {}'.format(myFamilyNames))

# TypeError: 'tuple' object does not support item assignment
# myFamilyNames[2] = '나'

# 실습2
todaySchedule = ('10시-업무 회의',
                 '12시-친구와 점심 약속',
                 '3시-자료 정리',
                 '6시-운동',
                 '9시-TV시청'
                 )
print('todaySchedule : {}'.format(todaySchedule))
