# 자료구조란 ?
## 여러개의 데이터가 묶여있는 자료형을 컨테이너 자료형이라고하고,
## 이러한 컨테이너 자료형의 데이터 구조를 자료구조라고 한다.

# 자료구조는 각각의 컨테이너 자료형에 따라 차이가 있으며,
# 파이썬의 대표적인 컨테이너 자료형으로는 리스트/튜플/딕셔너리/세트가 있다.

# 개별 데이터
student1 = '홍길동'
student2 = '박찬호'
student3 = '이용규'
student4 = '박승철'
student5 = '김지은'

# 리스트 (중복가능/수정가능)
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(students)
print(type(students))

for student in students:
    print(student)

# 튜플 (중복가능/수정불가)
students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
print(students)
print(type(students))

for student in students:
    print(student)

# 딕셔너리 (키와 벨류값)
scores = {'kor':95, 'eng':80, 'mat':100}
print(scores)
print(type(scores))

# 셋트 (키와 벨류값)
allSales = {100, 200, 500}
print(allSales)
print(type(allSales))

