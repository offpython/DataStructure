# 딕셔러니란?
## 키와 값을 이용해서 자료를 관리한다.

## 숫자/문자/논리형 + 컨테이너 자료형도 올 수 있다.
## 단, key에 immutable(변경불가능)값은 올 수 있지만 mutable값은 올 수 없다.

students = {'s1' : '홍길동', 's2': '박찬호', 's3': '이용규', 's4':{'박세리', '박공주'}}
print('students : {}'.format(students))
print('students : {}'.format(type(students)))

# 실습1
## 나의 정보(이름/전공/메일/주소 등)를 딕셔너리에 저장하고 출력
myInfo = {
    '이름': '박경진',
    '전공': 'computer',
    '메일': 'jin@naver.com',
    '학년': 3,
    '주소': '대한민국 서울',
    '취미': {'요리', '여행'},
}
print('myInfo : {}'.format(myInfo))
