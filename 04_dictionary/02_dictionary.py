# 딕셔너리 조회
## 딕셔너리는 키를 이용해서 값을 조회한다.
students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4': ['박세리', '박공주'], 's5':'김지은'}
print('students : {}'.format(students))

print(students['s1'])
print(students['s2'])
print(students['s3'])
print(students['s4'])
print(students['s4'][0])
print(students['s4'][1])

## 존재하지 않는 키를 이용한 조회시 에러 발생
#KeyError: 's6'
# print(students['s6'])

## get(key)를 이용해서 값을 구할 수 있다.
print(students.get('s1'))
print(students.get('s2'))
print(students.get('s3'))
## get()은 키가 없어도 에러 발생XX -> none으로 출
print(students.get('s6'))


# 실습1
## 나의 정보(이름/전공/메일/주소 등)를 딕셔너리에 저장하고 출력
myInfo = {
    '이름': '박경진',
    '전공': 'computer',
    '메일': 'jin@naver.com',
    '학년': 3,
    '주소': '대한민국 서울',
    '취미': ['요리', '여행']
}
print('myInfo : {}'.format(myInfo))

print(myInfo['이름'])
print(myInfo['메일'])
print(myInfo['취미'])
# KeyError: '주민번호'
# print(myInfo['주민번호'])

print(myInfo.get('전공'))
print(myInfo.get('학년'))
print(myInfo.get('주소'))

# get(key) -> None
print(myInfo.get('나이'))

